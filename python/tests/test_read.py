from snippets.read import (
    readint,
    readints,
    readintlist,
    readintlines,
    readintslines,
    readstr,
    readstrs,
    readstrlist,
    readstrlines,
    readintandstr,
    readstrandint,
    readintandstrlines,
    readstrandintlines
)
from parameterized import parameterized


def mock_input(*lines):
    it = iter(lines)
    return lambda: next(it)


@parameterized.expand(
    [
        (
            mock_input('1'),
            1
        ),
        (
            mock_input('0'),
            0
        ),
        (
            mock_input('-1'),
            -1
        )
    ]
)
def test_readint(input, expected):
    actual = readint.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('1 2'),
            (1, 2)
        ),
        (
            mock_input('0 -1'),
            (0, -1)
        ),
        (
            mock_input('3 3'),
            (3, 3)
        )
    ]
)
def test_readints(input, expected):
    actual = readints.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('1 2 3'),
            [1, 2, 3]
        ),
        (
            mock_input('-1'),
            [-1]
        ),
        (
            mock_input(''),
            []
        )
    ]
)
def test_readintlist(input, expected):
    actual = readintlist.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('1', '2', '3'),
            3,
            [1, 2, 3]
        ),
        (
            mock_input('-1'),
            1,
            [-1]
        ),
        (
            mock_input(),
            0,
            []
        )
    ]
)
def test_readintlines(input, N, expected):
    actual = readintlines.code(input, N)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('1 -1', '2 -2', '3 -3'),
            3,
            ((1, 2, 3), (-1, -2, -3))
        ),
        (
            mock_input('0 0'),
            1,
            ((0,), (0,))
        ),
        (
            mock_input(),
            0,
            ((), ())
        )
    ]
)
def test_readintslines(input, N, expected):
    actual = readintslines.code(input, N)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('wotsushi'),
            'wotsushi'
        ),
        (
            mock_input('WOTSUSHI'),
            'WOTSUSHI'
        ),
        (
            mock_input('31415'),
            '31415'
        ),
        (
            mock_input('...@..#+.'),
            '...@..#+.'
        ),
        (
            mock_input('wo tsu shi'),
            'wo tsu shi'
        ),
        (
            mock_input('Wo 2_shi!'),
            'Wo 2_shi!'
        ),
    ]
)
def test_readstr(input, expected):
    actual = readstr.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('wotsushi python'),
            ('wotsushi', 'python')
        ),
        (
            mock_input('WOTSUSHI PYTHON'),
            ('WOTSUSHI', 'PYTHON')
        ),
        (
            mock_input('31415 2718'),
            ('31415', '2718')
        ),
        (
            mock_input('...@..#+. .........'),
            ('...@..#+.', '.........')
        ),
        (
            mock_input('Wo2_shi! pYtHoN'),
            ('Wo2_shi!', 'pYtHoN')
        )
    ]
)
def test_readstrs(input, expected):
    actual = readstrs.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('wotsushi PYTHON Wo2_shi!'),
            ['wotsushi', 'PYTHON', 'Wo2_shi!']
        ),
        (
            mock_input('...@..#+.'),
            ['...@..#+.']
        ),
        (
            mock_input(''),
            []
        )
    ]
)
def test_readstrlist(input, expected):
    actual = readstrlist.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('wotsushi', 'PYTHON', 'Wo2_shi!'),
            3,
            ['wotsushi', 'PYTHON', 'Wo2_shi!']
        ),
        (
            mock_input('...@..#+.'),
            1,
            ['...@..#+.']
        ),
        (
            mock_input(''),
            0,
            []
        )
    ]
)
def test_readstrlines(input, N, expected):
    actual = readstrlines.code(input, N)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('1 wotsushi'),
            (1, 'wotsushi')
        ),
        (
            mock_input('0 ...@..#+.'),
            (0, '...@..#+.')
        ),
        (
            mock_input('-1 Wo2_shi!'),
            (-1, 'Wo2_shi!')
        )
    ]
)
def test_readintandstr(input, expected):
    actual = readintandstr.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('wotsushi 1'),
            ('wotsushi', 1)
        ),
        (
            mock_input('...@..#+. 0'),
            ('...@..#+.', 0)
        ),
        (
            mock_input('Wo2_shi! -1'),
            ('Wo2_shi!', -1)
        )
    ]
)
def test_readstrandint(input, expected):
    actual = readstrandint.code(input)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('1 wotsushi', '2 PYTHON', '3 Wo2_shi!'),
            3,
            ((1, 2, 3), ('wotsushi', 'PYTHON', 'Wo2_shi!'))
        ),
        (
            mock_input('0 ...@..#+.'),
            1,
            ((0,), ('...@..#+.',))
        ),
        (
            mock_input(),
            0,
            ((), ())
        )
    ]
)
def test_readintandstrlines(input, N, expected):
    actual = readintandstrlines.code(input, N)
    assert actual == expected


@parameterized.expand(
    [
        (
            mock_input('wotsushi 1', 'PYTHON 2', 'Wo2_shi! 3'),
            3,
            (('wotsushi', 'PYTHON', 'Wo2_shi!'), (1, 2, 3))
        ),
        (
            mock_input('...@..#+. 0'),
            1,
            (('...@..#+.',), (0,))
        ),
        (
            mock_input(),
            0,
            ((), ())
        )
    ]
)
def test_readstrandintlines(input, N, expected):
    actual = readstrandintlines.code(input, N)
    assert actual == expected
