import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_all_tuples_same_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), "All tuples have same length")

    def test_some_tuples_diff_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5), (7, 8, 9)], 3), "All tuples do not have same length")

    def test_empty_input(self):
        self.assertEqual(get_equal([], 0), "All tuples have same length")

    def test_negative_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)], -1), "All tuples do not have same length")

    def test_zero_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 0), "All tuples do not have same length")

    def test_non_tuple_in_input(self):
        with self.assertRaises(TypeError):
            get_equal([(1, 2, 3), "4, 5, 6", (7, 8, 9)], 3)
