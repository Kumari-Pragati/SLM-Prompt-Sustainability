import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_of_odd_Factors(10), 12)
        self.assertEqual(sum_of_odd_Factors(17), 18)
        self.assertEqual(sum_of_odd_Factors(25), 30)
        self.assertEqual(sum_of_odd_Factors(36), 55)

    def test_edge_cases(self):
        self.assertEqual(sum_of_odd_Factors(1), 2)
        self.assertEqual(sum_of_odd_Factors(2), 3)

    def test_corner_cases(self):
        self.assertEqual(sum_of_odd_Factors(0), 1)
        self.assertEqual(sum_of_odd_Factors(31), 32)
        self.assertEqual(sum_of_odd_Factors(85), 144)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_of_odd_Factors("abc")
        with self.assertRaises(ValueError):
            sum_of_odd_Factors(-10)
