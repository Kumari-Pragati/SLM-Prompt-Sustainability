import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(10), 11)
        self.assertEqual(sum_of_odd_Factors(15), 16)

    def test_edge_cases(self):
        self.assertEqual(sum_of_odd_Factors(0), 1)
        self.assertEqual(sum_of_odd_Factors(1), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum_of_odd_Factors(2**31 - 1), 2**31)
        self.assertEqual(sum_of_odd_Factors(2**31), 2**32)

    def test_corner_cases(self):
        self.assertEqual(sum_of_odd_Factors(3), 4)
        self.assertEqual(sum_of_odd_Factors(5), 6)
        self.assertEqual(sum_of_odd_Factors(7), 8)
