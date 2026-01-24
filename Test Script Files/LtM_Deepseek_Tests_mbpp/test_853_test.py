import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(3), 4)
        self.assertEqual(sum_of_odd_Factors(4), 6)
        self.assertEqual(sum_of_odd_Factors(5), 6)
        self.assertEqual(sum_of_odd_Factors(6), 10)
        self.assertEqual(sum_of_odd_Factors(7), 8)
        self.assertEqual(sum_of_odd_Factors(8), 15)
        self.assertEqual(sum_of_odd_Factors(9), 16)
        self.assertEqual(sum_of_odd_Factors(10), 21)

    def test_edge_conditions(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(0), 1)
        self.assertEqual(sum_of_odd_Factors(1000), 1000)

    def test_complex_cases(self):
        self.assertEqual(sum_of_odd_Factors(17), 18)
        self.assertEqual(sum_of_odd_Factors(100), 111)
        self.assertEqual(sum_of_odd_Factors(200), 225)
        self.assertEqual(sum_of_odd_Factors(300), 345)
