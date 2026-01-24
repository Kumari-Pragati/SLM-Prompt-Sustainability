import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(1, 4), (2, 5), (3, 6)])
        self.assertListEqual(zip_tuples((), ()), [])
        self.assertListEqual(zip_tuples((1,), (2,)), [(1, 2)])

    def test_edge_and_boundary(self):
        self.assertListEqual(zip_tuples((1, 2, 3), (4,)), [(1, 4), (2, None), (3, None)])
        self.assertListEqual(zip_tuples((1, 2, 3), ()), [(1, None), (2, None), (3, None)])
        self.assertListEqual(zip_tuples((1,), (2, 3)), [(1, 2), (None, 3)])
        self.assertListEqual(zip_tuples((1, 2, 3), (4, 4, 4)), [(1, 4), (2, 4), (3, 4)])

    def test_complex(self):
        self.assertListEqual(zip_tuples((1, 2, 3, 4), (5, 6, 7, 8)), [(1, 5), (2, 6), (3, 7), (4, 8)])
        self.assertListEqual(zip_tuples((1, 2, 3), (4, 4, 4, 4)), [(1, 4), (2, 4), (3, 4)])
        self.assertListEqual(zip_tuples((1, 2, 3, 4), (5, 5, 5)), [(1, 5), (2, 5), (3, 5), (4, None)])
