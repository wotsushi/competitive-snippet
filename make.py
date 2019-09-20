import yaml
import json
import os
import re
from typing import List
from itertools import takewhile, dropwhile, islice
from functools import reduce


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


if __name__ == "__main__":
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

# if __name__ == "__main__":
#     with open('langs.yml') as langs_yml:
#         langs = yaml.load(langs_yml, Loader=yaml.FullLoader)
#     for lang in langs:
#         lang_name = lang['lang']
#         ext = lang['ext']
#         with open(f'{lang_name}/{lang_name}.yml') as snippet_srcs:
#             snippet_list = yaml.load(snippet_srcs, Loader=yaml.FullLoader)
#         parser = importlib.import_module(f'{lang_name}.parser').parse
#         os.makedirs('json', exist_ok=True)
#         with open(f'json/{lang_name}.json', 'w') as snippets_json:
#             json.dump(
#                 {
#                     snippet['name']: {
#                         'prefix': snippet['prefix'],
#                         'description': snippet['description'],
#                         'body': parser(
#                             f'{lang_name}/snippets/{group["package"]}/'
#                             f'{snippet["name"]}.{ext}'
#                         )
#                     }
#                     for group in snippet_list
#                     for snippet in group['snippets']
#                 },
#                 snippets_json,
#                 indent=2
#             )
