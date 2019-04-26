import inspect
import importlib
import os
import re
from itertools import takewhile
from functools import reduce
from typing import List


def parse(src_path: str) -> List[str]:
    src_root, _ = os.path.splitext(src_path)
    _, src = inspect.getsource(
        importlib.import_module(
            src_root.replace('/', '.')
        ).code
    ).split(
        sep='\n',
        maxsplit=1
    )
    return [
        line[4:]
        for line in takewhile(
            lambda line: not line.startswith('    return'),
            reduce(
                lambda s, v: s.replace(
                    f'_{v[1]}',
                    f'${{{v[0]}:{v[1]}}}'
                ),
                enumerate(
                    iterable=dict.fromkeys(
                        re.findall(
                            pattern=r'\W_(\w+)',
                            string=src
                        )
                    ),
                    start=1
                ),
                src
            ).split('\n')
        )
    ]
