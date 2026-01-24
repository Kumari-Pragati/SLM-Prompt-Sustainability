import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_empty_tuples(self):
        self.assertListEqual(zip_tuples((), ()), [])

    def test_single_element_tuples(self):
        self.assertListEqual(zip_tuples((1,), (2,)), [(1, 2)])
        self.assertListEqual(zip_tuples((2,), (1,)), [(2, 1)])

    def test_equal_length_tuples(self):
        self.assertListEqual(zip_tuples((1, 2, 3), (a, b, c)), [(1, a), (2, b), (3, c)])
        self.assertListEqual(zip_tuples((a, b, c), (1, 2, 3)), [(a, 1), (b, 2), (c, 3)])

    def test_different_length_tuples(self):
        self.assertListEqual(zip_tuples((1, 2, 3), (a, b)), [(1, a), (2, b)])
        self.assertListEqual(zip_tuples((a, b), (1, 2, 3, 4)), [(a, 1), (b, 2)])

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: zip_tuples((1, 2, 3), (a, b)), -1)

    def test_index_larger_than_list_length(self):
        self.assertRaises(IndexError, lambda: zip_tuples((1, 2, 3), (a, b)), 4)
