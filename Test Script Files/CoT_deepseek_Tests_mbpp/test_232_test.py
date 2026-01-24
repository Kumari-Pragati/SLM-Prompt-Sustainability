import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 3), [5, 4, 3])

    def test_single_element(self):
        self.assertEqual(larg_nnum([5], 1), [5])

    def test_large_n(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])

    def test_negative_numbers(self):
        self.assertEqual(larg_nnum([-1, -2, -3, -4, -5], 3), [-1, -2, -3])

    def test_empty_list(self):
        self.assertEqual(larg_nnum([], 3), [])

    def test_large_n_greater_than_list_length(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5], 10), [5, 4, 3, 2, 1])

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            larg_nnum([1, 2, 3, 4, 5], -1)

    def test_invalid_list(self):
        with self.assertRaises(TypeError):
            larg_nnum("not a list", 1)
