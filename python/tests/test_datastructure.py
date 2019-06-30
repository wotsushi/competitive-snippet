from snippets.datastructure import union_find_tree, segment_tree
from parameterized import parameterized
from operator import add


def build_uft(n, p):
    UnionFindTree = union_find_tree.code()
    uft = UnionFindTree(n)
    for x, y in p:
        uft.union(x, y)
    return uft


uft_all_same = build_uft(
    5,
    [
        (1, 2),
        (2, 3),
        (4, 5),
        (5, 1)
    ]
)

uft_singletons = build_uft(
    3,
    []
)

uft_even_odd = build_uft(
    5,
    [
        (1, 3),
        (3, 5),
        (2, 4)
    ]
)


@parameterized.expand(
    [
        (
            uft_all_same,
            1,
            2,
            True
        ),
        (
            uft_all_same,
            2,
            3,
            True
        ),
        (
            uft_all_same,
            3,
            4,
            True
        ),
        (
            uft_all_same,
            4,
            5,
            True
        ),
        (
            uft_all_same,
            5,
            1,
            True
        ),
        (
            uft_singletons,
            1,
            2,
            False
        ),
        (
            uft_singletons,
            2,
            3,
            False
        ),
        (
            uft_singletons,
            3,
            1,
            False
        ),
        (
            uft_even_odd,
            1,
            3,
            True
        ),
        (
            uft_even_odd,
            2,
            4,
            True
        ),
        (
            uft_even_odd,
            3,
            5,
            True
        ),
        (
            uft_even_odd,
            1,
            2,
            False
        ),
        (
            uft_even_odd,
            2,
            3,
            False
        ),
        (
            uft_even_odd,
            3,
            4,
            False
        ),
        (
            uft_even_odd,
            4,
            5,
            False
        ),
    ]
)
def test_uft_same(uft, x, y, expected):
    actual = uft.same(x, y)
    assert actual == expected


@parameterized.expand(
    [
        (
            uft_all_same,
            1,
            5
        ),
        (
            uft_all_same,
            5,
            5
        ),
        (
            uft_singletons,
            1,
            1
        ),
        (
            uft_singletons,
            2,
            1
        ),
        (
            uft_singletons,
            3,
            1
        ),
        (
            uft_even_odd,
            1,
            3
        ),
        (
            uft_even_odd,
            2,
            2
        ),
        (
            uft_even_odd,
            3,
            3
        ),
        (
            uft_even_odd,
            4,
            2
        ),
        (
            uft_even_odd,
            5,
            3
        ),
    ]
)
def test_uft_size(uft, x, expected):
    actual = uft.size(x)
    assert actual == expected


def build_segtree(n, f, e, q):
    SegmentTree = segment_tree.code()
    segtree = SegmentTree(n, f, e)
    for i, x in q:
        segtree[i] = x
    return segtree


rmq = build_segtree(
    8,
    min,
    10**18,
    [
        (1, 5),
        (2, 3),
        (3, 7),
        (4, 9),
        (5, 6),
        (6, 4),
        (7, 1),
        (8, 2)
    ]
)
updated_rmq = build_segtree(
    8,
    min,
    10**18,
    [
        (1, 5),
        (2, 3),
        (3, 7),
        (4, 9),
        (5, 6),
        (6, 4),
        (7, 1),
        (8, 2),
        (4, 0)
    ]
)
bit = build_segtree(
    8,
    add,
    0,
    [
        (1, 5),
        (2, 3),
        (3, 7),
        (4, 9),
        (5, 6),
        (6, 4),
        (7, 1),
        (8, 2)
    ]
)
updated_bit = build_segtree(
    8,
    add,
    0,
    [
        (1, 5),
        (2, 3),
        (3, 7),
        (4, 9),
        (5, 6),
        (6, 4),
        (7, 1),
        (8, 2),
        (4, 10)
    ]
)
not_pow_of_2_rmq = build_segtree(
    3,
    min,
    10**18,
    [
        (1, 5),
        (2, 3),
        (3, 7)
    ]
)
updated_not_pow_of_2_rmq = build_segtree(
    3,
    min,
    10**18,
    [
        (1, 5),
        (2, 3),
        (3, 7),
        (2, 6),
        (3, 4),
    ]
)


@parameterized.expand(
    [
        (
            rmq,
            slice(1, 9),
            1
        ),
        (
            rmq,
            slice(1, 4),
            3
        ),
        (
            rmq,
            slice(4, 6),
            6
        ),
        (
            rmq,
            slice(3, 4),
            7
        ),
        (
            updated_rmq,
            slice(1, 9),
            0
        ),
        (
            updated_rmq,
            slice(1, 4),
            3
        ),
        (
            updated_rmq,
            slice(4, 6),
            0
        ),
        (
            updated_rmq,
            slice(3, 4),
            7
        ),
        (
            bit,
            slice(1, 2),
            5
        ),
        (
            bit,
            slice(1, 3),
            8
        ),
        (
            bit,
            slice(1, 4),
            15
        ),
        (
            bit,
            slice(1, 5),
            24
        ),
        (
            bit,
            slice(1, 9),
            37
        ),
        (
            updated_bit,
            slice(1, 2),
            5
        ),
        (
            updated_bit,
            slice(1, 3),
            8
        ),
        (
            updated_bit,
            slice(1, 4),
            15
        ),
        (
            updated_bit,
            slice(1, 5),
            25
        ),
        (
            updated_bit,
            slice(1, 9),
            38
        ),
        (
            not_pow_of_2_rmq,
            slice(1, 2),
            5
        ),
        (
            not_pow_of_2_rmq,
            slice(1, 3),
            3
        ),
        (
            not_pow_of_2_rmq,
            slice(1, 4),
            3
        ),
        (
            not_pow_of_2_rmq,
            slice(2, 3),
            3
        ),
        (
            not_pow_of_2_rmq,
            slice(2, 4),
            3
        ),
        (
            not_pow_of_2_rmq,
            slice(3, 4),
            7
        ),
        (
            updated_not_pow_of_2_rmq,
            slice(1, 2),
            5
        ),
        (
            updated_not_pow_of_2_rmq,
            slice(1, 3),
            5
        ),
        (
            updated_not_pow_of_2_rmq,
            slice(1, 4),
            4
        ),
        (
            updated_not_pow_of_2_rmq,
            slice(2, 3),
            6
        ),
        (
            updated_not_pow_of_2_rmq,
            slice(2, 4),
            4
        ),
        (
            updated_not_pow_of_2_rmq,
            slice(3, 4),
            4
        )
    ]
)
def test_segtree(segtree, s, expected):
    actual = segtree[s]
    assert actual == expected
