import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOdd_Length_Sum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 15)

    def test_edge_case_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_edge_case_even_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 6)

    def test_edge_case_odd_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6]), 15)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum("Invalid input")

    def test_invalid_input_non_integer_list(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum([1, 2, "Invalid input", 4])
