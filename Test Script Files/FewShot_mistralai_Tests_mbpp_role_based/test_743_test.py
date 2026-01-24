import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])

    def test_empty_list(self):
        self.assertEqual(rotate_right([], 2, 3), [])

    def test_single_element_list(self):
        self.assertEqual(rotate_right([1], 2, 3), [1])

    def test_negative_m(self):
        self.assertEqual(rotate_right([1, 2, 3], -1, 3), [3])

    def test_negative_n(self):
        self.assertEqual(rotate_right([1, 2, 3], 2, -1), [1, 2])

    def test_m_greater_than_list_length(self):
        self.assertEqual(rotate_right([1, 2, 3], 4, 3), [3, 1, 2])

    def test_n_greater_than_list_length(self):
        self.assertEqual(rotate_right([1, 2, 3], 2, 4), [3, 1, 2])
