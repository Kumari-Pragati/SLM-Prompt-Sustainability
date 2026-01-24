import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(rotate_right([], 1, 1), [])

    def test_single_element(self):
        self.assertEqual(rotate_right([1], 1, 1), [1])

    def test_simple_list(self):
        self.assertEqual(rotate_right([1, 2, 3, 4], 2, 2), [4, 1, 2, 3])

    def test_large_list(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 3), [8, 9, 1, 2, 3, 4, 5, 6, 7])

    def test_negative_m(self):
        self.assertEqual(rotate_right([1, 2, 3], -1, 1), [3, 1, 2])

    def test_negative_n(self):
        self.assertEqual(rotate_right([1, 2, 3], 1, -1), [1, 2, 3])

    def test_zero_m(self):
        self.assertEqual(rotate_right([1, 2, 3], 0, 1), [3])

    def test_zero_n(self):
        self.assertEqual(rotate_right([1, 2, 3], 1, 0), [1, 2])

    def test_m_greater_than_len(self):
        self.assertEqual(rotate_right([1, 2, 3], len([1, 2, 3]) + 1, 1), [2, 3, 1])

    def test_n_greater_than_len(self):
        self.assertEqual(rotate_right([1, 2, 3], 1, len([1, 2, 3]) + 1), [1])
