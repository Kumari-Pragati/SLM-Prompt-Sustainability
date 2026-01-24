import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_all_tuples_same_length(self):
        input_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        self.assertEqual(get_equal(input_list, 3), "All tuples have same length")

    def test_all_tuples_diff_length(self):
        input_list = [(1, 2, 3), (4, 5), (7, 8, 9, 10)]
        self.assertEqual(get_equal(input_list, 3), "All tuples do not have same length")

    def test_empty_list(self):
        input_list = []
        self.assertEqual(get_equal(input_list, 3), "All tuples do not have same length")

    def test_single_tuple(self):
        input_list = [(1, 2, 3)]
        self.assertEqual(get_equal(input_list, 3), "All tuples have same length")

    def test_k_is_zero(self):
        input_list = [(1, 2, 3)]
        with self.assertRaises(ValueError):
            get_equal(input_list, 0)
