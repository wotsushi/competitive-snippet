import click
import subprocess
import glob
import os
import pytest
from parameterized import parameterized


@parameterized.expand([
    (
        f'{snippet_name}_{serial}',
        f'{snippet_dir}/{snippet_name}',
        snippet_name,
        os.path.basename(serial)
    )
    for snippet_dir, snippet_name in map(
        os.path.split,
        glob.glob(f'snippets/*/*')
    )
    for serial in sorted(
        map(
            os.path.basename,
            glob.glob(f'{snippet_dir}/{snippet_name}/in/*')
        )
    )
])
def test_rust(name, snippet_path, snippet_name, serial):
    subprocess.run(
        args=[
            'rustup',
            'run',
            '1.15.1',
            'rustc',
            f'{snippet_path}/{snippet_name}.rs',
            '-o',
            f'{snippet_path}/{snippet_name}.out'
        ]
    )
    with open(f'{snippet_path}/in/{serial}') as input_test,\
            open(f'{snippet_path}/out/{serial}') as ans_test:
        actual = subprocess.run(
            args=f'{snippet_path}/{snippet_name}.out',
            stdin=input_test,
            capture_output=True
        ).stdout.decode()
        expected = ans_test.read()
        assert actual == expected


@click.command()
@click.option('-s', '--snippet', default=None)
def main(snippet):
    pytest.main(
        ['judge.py', '-k', f'{snippet}_', '--tb=short'] if snippet else
        ['judge.py', '--tb=short']
    )


if __name__ == "__main__":
    main()
