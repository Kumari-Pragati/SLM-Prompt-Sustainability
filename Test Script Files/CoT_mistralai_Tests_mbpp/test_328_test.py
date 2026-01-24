import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rotate_left([], 0, 0), [])

    def test_single_element(self):
        self.assertEqual(rotate_left([1], 0, 1), [])
        self.assertEqual(rotate_left([1], 1, 0), [1])

    def test_simple_list(self):
        self.assertEqual(rotate_left([1, 2, 3, 4], 2, 2), [4, 1, 2, 3])
        self.assertEqual(rotate_left([1, 2, 3, 4], 0, 4), [4, 1, 2, 3])
        self.assertEqual(rotate_left([1, 2, 3, 4], 4, 0), [3, 4, 1, 2])

    def test_negative_m_or_n(self):
        self.assertEqual(rotate_left([1, 2, 3], -1, 2), [2, 3])
        self.assertEqual(rotate_left([1, 2, 3], 1, -1), [1, 3])

    def test_m_greater_than_len(self):
        self.assertEqual(rotate_left([1, 2, 3], 4, 2), [3, 1, 2])

    def test_n_greater_than_len(self):
        self.assertEqual(rotate_left([1, 2, 3], 1, 4), [3, 1, 2])
