import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativenum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sum_negativenum([-1, -2, 3, 4, 5]), -3)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_edge_case_single_negative_number(self):
        self.assertEqual(sum_negativenum([-1]), -1)

    def test_edge_case_single_positive_number(self):
        self.assertEqual(sum_negativenum([1]), 0)

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(sum_negativenum([-1, 2, -3, 4, -5]), -3)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sum_negativenum("Invalid input")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            sum_negativenum([1, "Invalid input", 3])
