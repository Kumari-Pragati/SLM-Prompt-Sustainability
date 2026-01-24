import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_all_tuples_same_length(self):
        self.assertEqual(get_equal([(1, 2), (3, 4), (5, 6)], 2), "All tuples have same length")

    def test_not_all_tuples_same_length(self):
        self.assertEqual(get_equal([(1, 2), (3, 4, 5), (6,)], 2), "All tuples do not have same length")

    def test_empty_input(self):
        self.assertEqual(get_equal([], 2), "All tuples do not have same length")

    def test_zero_k(self):
        self.assertEqual(get_equal([(1, 2), (3, 4), (5, 6)], 0), "All tuples do not have same length")
