import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5]), 10.0)

    def test_edge_case_zero_length(self):
        self.assertEqual(round_and_sum([]), 0.0)

    def test_edge_case_single_element(self):
        self.assertEqual(round_and_sum([1.5]), 1.5)

    def test_edge_case_multiple_elements(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5, 4.5]), 12.0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(round_and_sum([-1.5, -2.5, -3.5]), -7.5)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5, 4.5, 5.5]), 15.0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            round_and_sum("Invalid input")

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, "Invalid input", 3])
