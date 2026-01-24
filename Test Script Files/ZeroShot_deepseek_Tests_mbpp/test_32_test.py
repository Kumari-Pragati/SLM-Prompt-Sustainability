import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_max_Prime_Factors(self):
        self.assertEqual(max_Prime_Factors(10), 5)
        self.assertEqual(max_Prime_Factors(17), 17)
        self.assertEqual(max_Prime_Factors(315), 7)
        self.assertEqual(max_Prime_Factors(13), 13)
        self.assertEqual(max_Prime_Factors(1), -1)
        self.assertEqual(max_Prime_Factors(0), -1)
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(100), 5)
        self.assertEqual(max_Prime_Factors(81), 3)
        self.assertEqual(max_Prime_Factors(1000), 5)
