import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(func([], 3), [])

    def test_single_row(self):
        self.assertEqual(func([[1, 2, 3]], 3), [1, 2, 3])

    def test_multiple_rows(self):
        self.assertEqual(func([[1, 2, 3], [3, 2, 1], [2, 1, 3]], 3), [1, 2, 3])

    def test_k_greater_than_length(self):
        self.assertEqual(func([[1, 2, 3], [3, 2, 1], [2, 1, 3]], 10), [1, 2, 3])

    def test_k_equal_to_length(self):
        self.assertEqual(func([[1, 2, 3], [3, 2, 1], [2, 1, 3]], 3), [1, 2, 3])

    def test_k_less_than_length(self):
        self.assertEqual(func([[1, 2, 3], [3, 2, 1], [2, 1, 3]], 2), [1, 2])

    def test_k_zero(self):
        self.assertEqual(func([[1, 2, 3], [3, 2, 1], [2, 1, 3]], 0), [])

    def test_k_negative(self):
        with self.assertRaises(ValueError):
            func([[1, 2, 3], [3, 2, 1], [2, 1, 3]], -1)
