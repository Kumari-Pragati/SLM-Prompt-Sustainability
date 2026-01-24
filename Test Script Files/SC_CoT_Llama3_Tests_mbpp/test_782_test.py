import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOdd_Length_Sum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 9)

    def test_edge_case_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_edge_case_even_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 6)

    def test_edge_case_odd_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6]), 15)

    def test_edge_case_zero_length_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5]), -15)

    def test_edge_case_mixed_positive_and_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, 3, 4, 5]), 6)

    def test_edge_case_non_integer_numbers(self):
        self.assertEqual(Odd_Length_Sum([1.0, 2.0, 3.0, 4.0, 5.0]), 15.0)

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum(['a', 'b', 'c', 'd', 'e'])
