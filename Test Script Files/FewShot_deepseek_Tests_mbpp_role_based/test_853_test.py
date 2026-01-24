import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_of_odd_Factors(36), 10)

    def test_edge_case(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_boundary_case(self):
        self.assertEqual(sum_of_odd_Factors(2), 3)

    def test_large_number(self):
        self.assertEqual(sum_of_odd_Factors(1000), 13)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_of_odd_Factors("abc")

        with self.assertRaises(ValueError):
            sum_of_odd_Factors(-5)
