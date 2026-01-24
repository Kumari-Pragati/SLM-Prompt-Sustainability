import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6]], 2), [5, 6])
    def test_empty_input(self):
        self.assertEqual(func([], 2), [])
    def test_single_row(self):
        self.assertEqual(func([[1, 2, 3]], 1), [1])
    def test_k_zero(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6]], 0), [])
    def test_k_greater_than_length(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6]], 5), [6, 6, 6, 6, 6])
    def test_k_equal_to_length(self):
        self.assertEqual(func([[1, 2, 3], [4, 5, 6]], 3), [6, 5, 4])
    def test_k_greater_than_length_with_duplicates(self):
        self.assertEqual(func([[1, 2, 2, 3], [4, 5, 5, 6]], 4), [6, 6, 5, 4])
