import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(1, 4), (2, 5), (3, 6)])

    def test_edge_case_short_list(self):
        self.assertListEqual(zip_tuples((1, 2), (3, 4)), [(1, 3), (2, 4)])

    def test_edge_case_long_list(self):
        self.assertListEqual(zip_tuples((1, 2, 3, 4), (5, 6)), [(1, 5), (2, 6), (3, None), (4, None)])

    def test_corner_case_empty_list(self):
        self.assertListEqual(zip_tuples((), (1, 2, 3)), [])
