import re
from itertools import takewhile, dropwhile
from functools import reduce
from typing import List


def parse(src_path: str) -> List[str]:
    with open(src_path) as src_file:
        src = '\n'.join(
            [
                line.rstrip()
                for line in takewhile(
                    lambda line: not line.startswith('    return'),
                    dropwhile(
                        lambda line: not line.startswith('def code'),
                        src_file
                    )
                )
            ][1:]
        )
    return [
        line[4:]
        for line in reduce(
            lambda s, v: s.replace(
                f'_{v[1]}',
                f'${{{v[0]}:{v[1]}}}'
            ),
            enumerate(
                iterable=dict.fromkeys(
                    re.findall(
                        pattern=r'\W_([a-zA-Z0-9]+)',
                        string=src
                    )
                ),
                start=1
            ),
            src
        ).split('\n')
    ]
