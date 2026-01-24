import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 46)

    def test_edge_case_single_element(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_boundary_case_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_boundary_case_large_list(self):
        self.assertEqual(Odd_Length_Sum(list(range(1, 10001))), 1666566650000)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum('not a list')

    def test_invalid_input_integer(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum(123)
