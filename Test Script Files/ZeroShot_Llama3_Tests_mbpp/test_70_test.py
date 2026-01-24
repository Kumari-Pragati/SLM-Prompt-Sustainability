import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_get_equal_same_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), "All tuples have same length")

    def test_get_equal_diff_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5), (7, 8, 9, 10)], 3), "All tuples do not have same length")

    def test_get_equal_empty_list(self):
        self.assertEqual(get_equal([], 3), "All tuples do not have same length")

    def test_get_equal_single_tuple(self):
        self.assertEqual(get_equal([(1, 2, 3)], 3), "All tuples have same length")

    def test_get_equal_no_tuples(self):
        self.assertEqual(get_equal([], 0), "All tuples do not have same length")
