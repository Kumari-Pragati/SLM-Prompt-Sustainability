import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):

    def test_typical_positive_numbers(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_typical_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

    def test_typical_mixed_numbers(self):
        self.assertEqual(sum_positivenum([1, -2, 3, -4, 5]), 5)

    def test_edge_case_single_positive(self):
        self.assertEqual(sum_positivenum([1]), 1)

    def test_edge_case_single_negative(self):
        self.assertEqual(sum_positivenum([-1]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_edge_case_single_zero(self):
        self.assertEqual(sum_positivenum([0]), 0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sum_positivenum("invalid input")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            sum_positivenum([1, "invalid input", 3])
