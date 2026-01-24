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

    def test_different_length_tuples_short(self):
        self.assertListEqual(zip_tuples((1, 2), (a, b, c)), [(1, a), (2, b)])

    def test_different_length_tuples_long(self):
        self.assertListEqual(zip_tuples((1, 2, 3), (a, b)), [(1, a), (2, b)])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            zip_tuples((1, 2), (-1,))

    def test_out_of_bound_index(self):
        with self.assertRaises(IndexError):
            zip_tuples((1, 2, 3), (a, b, c, d))
