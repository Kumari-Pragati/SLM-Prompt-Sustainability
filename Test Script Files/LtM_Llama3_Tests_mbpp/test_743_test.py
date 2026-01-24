import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])
    def test_empty_input(self):
        self.assertEqual(rotate_right([], 2, 1), [])
    def test_single_element_input(self):
        self.assertEqual(rotate_right([1], 1, 1), [1])
    def test_rotate_by_zero(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 1), [1, 2, 3, 4, 5])
    def test_rotate_by_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 1), [1, 2, 3, 4, 5])
    def test_rotate_by_greater_than_length(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 6, 1), [1, 2, 3, 4, 5])
