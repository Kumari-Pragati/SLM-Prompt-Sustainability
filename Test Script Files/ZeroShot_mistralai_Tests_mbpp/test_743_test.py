import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rotate_right([], 1, 1), [])

    def test_single_element(self):
        self.assertEqual(rotate_right([1], 1, 1), [1])

    def test_simple_list(self):
        self.assertEqual(rotate_right([1, 2, 3, 4], 2, 2), [3, 4, 1, 2])

    def test_negative_m_or_n(self):
        self.assertEqual(rotate_right([1, 2, 3, 4], -1, 2), [3, 4, 1, 2])
        self.assertEqual(rotate_right([1, 2, 3, 4], 2, -1), [3, 4, 1, 2])

    def test_m_greater_than_len(self):
        self.assertEqual(rotate_right([1, 2, 3, 4], 5, 2), [3, 4, 1, 2])

    def test_n_greater_than_len(self):
        self.assertEqual(rotate_right([1, 2, 3, 4], 1, 5), [3, 4, 1, 2])
