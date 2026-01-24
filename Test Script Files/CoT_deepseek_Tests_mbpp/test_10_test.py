import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 3), [1, 2, 3])

    def test_small_n(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 1), [1])

    def test_large_n(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 5), [1, 2, 3, 4, 5])

    def test_duplicate_values(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4, 1, 2, 3], 3), [1, 1, 2])

    def test_negative_values(self):
        self.assertEqual(small_nnum([-3, -1, -2, -5, -4], 3), [-5, -4, -3])

    def test_empty_list(self):
        self.assertEqual(small_nnum([], 3), [])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            small_nnum([3, 1, 2, 5, 4], -1)

    def test_invalid_list(self):
        with self.assertRaises(TypeError):
            small_nnum("not a list", 3)
