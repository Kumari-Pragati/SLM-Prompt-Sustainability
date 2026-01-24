import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 32)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5]), -32)
        self.assertEqual(Odd_Length_Sum([0, 0, 0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)
        self.assertEqual(Odd_Length_Sum([-1]), -1)

    def test_edge_case_even_length(self):
        self.assertEqual(Odd_Length_Sum([1, 2]), 3)
        self.assertEqual(Odd_Length_Sum([-1, -2]), -3)
