import click
import requests
import os
import shutil
import glob
import yaml
import json
import pytest
import re
from typing import List
from itertools import takewhile, dropwhile, islice
from functools import reduce


ENDPOINT = "https://judgedat.u-aizu.ac.jp"


def parse(src_path: str) -> List[str]:
    with open(src_path) as src_file:
        src = "\n".join(
            [
                line.rstrip()
                for line in takewhile(
                    lambda line: "// snip" not in line,
                    islice(
                        dropwhile(lambda line: "// snip" not in line, src_file), 1, None
                    ),
                )
            ]
        )
    return [
        line[4:]
        for line in reduce(
            lambda s, v: s.replace(f"_{v[1]}", f"${{{v[0]}:{v[1]}}}"),
            enumerate(
                iterable=dict.fromkeys(
                    re.findall(pattern=r"\W_([a-zA-Z0-9]+)", string=src)
                ),
                start=1,
            ),
            src,
        ).split("\n")
    ]


@click.group()
def snip():
    pass


@snip.command()
def create():
    package_name = click.prompt("package name")
    snippet_name = click.prompt("snippet name")
    extention = click.prompt("extention", default="rs")
    prefix = click.prompt("prefix")
    description = click.prompt("description")

    snippet_dir = f"snippets/{package_name}/{snippet_name}"
    os.makedirs(snippet_dir, exist_ok=True)
    with open(f"{snippet_dir}/{snippet_name}.{extention}", "w"):
        pass
    # TODO: Generaize
    with open("rust.yml", "r") as snippet_yml:
        snippets = yaml.load(snippet_yml, Loader=yaml.FullLoader)
    package = next(
        (package for package in snippets if package["package"] == package_name), None
    )
    if package:
        package["snippets"].append(
            {"name": snippet_name, "prefix": f"${prefix}", "description": description}
        )
    else:
        snippets.append(
            {
                "package": package_name,
                "snippets": [
                    {
                        "name": snippet_name,
                        "prefix": f"${prefix}",
                        "description": description,
                    }
                ],
            }
        )
    with open("rust.yml", "w") as snippet_yml:
        yaml.dump(snippets, snippet_yml, default_flow_style=False)


@snip.command()
@click.argument("deleted_snippet")
def delete(deleted_snippet):
    snippet_dir = next(iter(glob.glob(f"snippets/**/{deleted_snippet}")))
    shutil.rmtree(snippet_dir, ignore_errors=True)
    with open("rust.yml", "r") as snippet_yml:
        snippets = yaml.load(snippet_yml, Loader=yaml.FullLoader)
    removed_snippets = [
        {
            "package": group["package"],
            "snippets": [
                snippet
                for snippet in group["snippets"]
                if snippet["name"] != deleted_snippet
            ],
        }
        for group in snippets
    ]
    with open("rust.yml", "w") as snippet_yml:
        yaml.dump(removed_snippets, snippet_yml, default_flow_style=False)


@snip.command()
@click.argument("snippet")
@click.argument("problem_id")
def pull(snippet, problem_id):
    snippet_dir = next(iter(glob.glob(f"snippets/**/{snippet}")))
    in_dir = f"{snippet_dir}/in"
    shutil.rmtree(in_dir, ignore_errors=True)
    os.makedirs(in_dir)
    out_dir = f"{snippet_dir}/out"
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir)

    res = requests.get(f"{ENDPOINT}/testcases/{problem_id}/header").json()
    serials = [header["serial"] for header in res["headers"]]
    for serial in serials:
        testcase = requests.get(f"{ENDPOINT}/testcases/{problem_id}/{serial}").json()
        if "terminated" not in testcase["in"] and "terminated" not in testcase["out"]:
            with open(f"{in_dir}/{serial:02}", "w") as in_testcase:
                in_testcase.write(testcase["in"])
            with open(f"{out_dir}/{serial:02}", "w") as out_testcase:
                out_testcase.write(testcase["out"])


@snip.command()
@click.option("-s", "--snippet", default=None)
def test(snippet):
    pytest.main(
        ["test.py", "-k", f"{snippet}_", "--tb=short"]
        if snippet
        else ["test.py", "--tb=short"]
    )


@snip.command()
def build():
    with open("rust.yml") as snippet_yml:
        snippets = yaml.load(snippet_yml, Loader=yaml.FullLoader)
    os.makedirs("json", exist_ok=True)
    with open(f"json/rust.json", "w") as snippets_json:
        json.dump(
            {
                snippet["name"]: {
                    "prefix": snippet["prefix"],
                    "description": snippet["description"],
                    "body": parse(
                        f'snippets/{group["package"]}/{snippet["name"]}/'
                        f'{snippet["name"]}.rs'
                    ),
                }
                for group in snippets
                for snippet in group["snippets"]
            },
            snippets_json,
            indent=2,
        )


if __name__ == "__main__":
    snip()
