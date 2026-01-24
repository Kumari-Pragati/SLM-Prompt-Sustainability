import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(3), 4)
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(5), 5)
        self.assertEqual(sum_of_odd_Factors(6), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_of_odd_Factors(0), 1)
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(3), 4)
        self.assertEqual(sum_of_odd_Factors(4), 4)
        self.assertEqual(sum_of_odd_Factors(5), 5)
        self.assertEqual(sum_of_odd_Factors(6), 6)
        self.assertEqual(sum_of_odd_Factors(7), 8)
        self.assertEqual(sum_of_odd_Factors(8), 8)
        self.assertEqual(sum_of_odd_Factors(9), 10)
        self.assertEqual(sum_of_odd_Factors(10), 12)

    def test_complex_and_corner_cases(self):
        self.assertEqual(sum_of_odd_Factors(11), 12)
        self.assertEqual(sum_of_odd_Factors(12), 12)
        self.assertEqual(sum_of_odd_Factors(13), 14)
        self.assertEqual(sum_of_odd_Factors(14), 14)
        self.assertEqual(sum_of_odd_Factors(15), 16)
        self.assertEqual(sum_of_odd_Factors(16), 16)
        self.assertEqual(sum_of_odd_Factors(17), 18)
        self.assertEqual(sum_of_odd_Factors(18), 18)
        self.assertEqual(sum_of_odd_Factors(19), 20)
        self.assertEqual(sum_of_odd_Factors(20), 20)
