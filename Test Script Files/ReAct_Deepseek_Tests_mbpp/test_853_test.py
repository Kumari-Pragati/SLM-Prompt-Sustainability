import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(2), 3)
        self.assertEqual(sum_of_odd_Factors(3), 4)
        self.assertEqual(sum_of_odd_Factors(4), 6)
        self.assertEqual(sum_of_odd_Factors(5), 6)
        self.assertEqual(sum_of_odd_Factors(6), 10)
        self.assertEqual(sum_of_odd_Factors(7), 11)
        self.assertEqual(sum_of_odd_Factors(8), 15)
        self.assertEqual(sum_of_odd_Factors(9), 16)
        self.assertEqual(sum_of_odd_Factors(10), 21)

    def test_edge_cases(self):
        self.assertEqual(sum_of_odd_Factors(1), 1)
        self.assertEqual(sum_of_odd_Factors(0), 1)
        self.assertEqual(sum_of_odd_Factors(100), 121)
        self.assertEqual(sum_of_odd_Factors(1000), 1321)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            sum_of_odd_Factors('a')
        with self.assertRaises(ValueError):
            sum_of_odd_Factors(-1)
