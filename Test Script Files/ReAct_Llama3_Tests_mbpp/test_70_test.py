import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_all_tuples_same_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), "All tuples have same length")

    def test_all_tuples_diff_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5), (7, 8, 9, 10)], 3), "All tuples do not have same length")

    def test_empty_input(self):
        self.assertEqual(get_equal([], 3), "All tuples do not have same length")

    def test_single_tuple(self):
        self.assertEqual(get_equal([(1, 2, 3)], 3), "All tuples have same length")

    def test_k_is_zero(self):
        with self.assertRaises(ValueError):
            get_equal([(1, 2, 3)], 0)

    def test_k_is_negative(self):
        with self.assertRaises(ValueError):
            get_equal([(1, 2, 3)], -1)
