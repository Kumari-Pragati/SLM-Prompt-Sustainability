import unittest
from70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_same_length_tuples(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3), (1, 2, 3)], 3), "All tuples have same length")
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3), (1, 2, 3, 4)], 3), "All tuples do not have same length")

    def test_empty_list(self):
        self.assertEqual(get_equal([], 3), "All tuples do not have same length")

    def test_single_tuple(self):
        self.assertEqual(get_equal([(1, 2, 3)], 3), "All tuples have same length")
        self.assertEqual(get_equal([(1, 2, 3)], 4), "All tuples do not have same length")

    def test_mixed_length_tuples(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2)], 3), "All tuples do not have same length")
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3, 4)], 3), "All tuples do not have same length")

    def test_negative_k(self):
        self.assertRaises(ValueError, get_equal, [(1, 2, 3)], -1)
