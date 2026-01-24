import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(3), 3)
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(5), 5)
        self.assertEqual(max_Prime_Factors(6), 2)
        self.assertEqual(max_Prime_Factors(7), 7)
        self.assertEqual(max_Prime_Factors(8), 2)
        self.assertEqual(max_Prime_Factors(9), 3)
        self.assertEqual(max_Prime_Factors(10), 2)

    def test_edge(self):
        self.assertEqual(max_Prime_Factors(1), 1)
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(3), 3)
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(5), 5)
        self.assertEqual(max_Prime_Factors(6), 2)
        self.assertEqual(max_Prime_Factors(7), 7)
        self.assertEqual(max_Prime_Factors(8), 2)
        self.assertEqual(max_Prime_Factors(9), 3)
        self.assertEqual(max_Prime_Factors(10), 2)

    def test_complex(self):
        self.assertEqual(max_Prime_Factors(11), 11)
        self.assertEqual(max_Prime_Factors(12), 2)
        self.assertEqual(max_Prime_Factors(13), 13)
        self.assertEqual(max_Prime_Factors(14), 2)
        self.assertEqual(max_Prime_Factors(15), 3)
        self.assertEqual(max_Prime_Factors(16), 2)
        self.assertEqual(max_Prime_Factors(17), 17)
        self.assertEqual(max_Prime_Factors(18), 2)
        self.assertEqual(max_Prime_Factors(19), 19)
        self.assertEqual(max_Prime_Factors(20), 2)
