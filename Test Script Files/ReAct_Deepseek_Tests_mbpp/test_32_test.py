import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_Prime_Factors(315), 7)
        self.assertEqual(max_Prime_Factors(100), 5)
        self.assertEqual(max_Prime_Factors(13), 13)
        self.assertEqual(max_Prime_Factors(1), 1)

    def test_edge_cases(self):
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(97), 97)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(max_Prime_Factors(0), -1)
        self.assertEqual(max_Prime_Factors(-1), -1)
        self.assertEqual(max_Prime_Factors(-10), -1)
