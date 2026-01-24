import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rotate_left([], 0, 1), [])
        self.assertEqual(rotate_list([], 1, 0), [])

    def test_single_element(self):
        self.assertEqual(rotate_left([1], 0, 1), [])
        self.assertEqual(rotate_left([1], 1, 0), [1])

    def test_simple_list(self):
        self.assertEqual(rotate_left([1, 2, 3, 4], 1, 3), [4, 1, 2, 3])
        self.assertEqual(rotate_left([1, 2, 3, 4], 3, 1), [3, 4, 1, 2])

    def test_negative_m_or_n(self):
        with self.assertRaises(ValueError):
            rotate_left([1, 2, 3], -1, 1)
        with self.assertRaises(ValueError):
            rotate_left([1, 2, 3], 1, -1)

    def test_m_greater_than_len(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3], len([1, 2, 3]) + 1, 1)

    def test_n_greater_than_len(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3], 1, len([1, 2, 3]) + 1)
