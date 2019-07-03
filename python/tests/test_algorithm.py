from snippets.algorithm import bisectionmethod
from parameterized import parameterized


@parameterized.expand(
    [
        (lambda n: n**3 < 30, 0, 10**18, 3),
        (lambda n: n**3 > 30, 10**18, 0, 4),
        (lambda n: n**3 < 30, 3, 10**18, 3),
        (lambda n: n**3 > 30, 4, 0, 4),
        (lambda n: n**3 < 30, 3, 4, 3),
    ]
)
def test_bis(p, ok, ng, expected):
    bis = bisectionmethod.code()
    actual = bis(p, ok, ng)
    assert actual == expected
