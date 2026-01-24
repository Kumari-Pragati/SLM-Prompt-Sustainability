import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositiveNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_positivenum([-1, 2, -3, 4]), 5)

    def test_zero(self):
        self.assertEqual(sum_positivenum([0]), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_positivenum([1000000, 2000000, 3000000]), 6000000)

    def test_float_numbers(self):
        self.assertAlmostEqual(sum_positivenum([1.5, 2.5, 3.5]), 7.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            sum_positivenum(['1', '2', '3'])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            sum_positivenum(None)
