import unittest
from mbpp_32_code import sqrt

def max_Prime_Factors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)

class TestMaxPrimeFactors(unittest.TestCase):

    def test_simple_numbers(self):
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(3), 3)
        self.assertEqual(max_Prime_Factors(4), 2)
        self.assertEqual(max_Prime_Factors(5), 5)
        self.assertEqual(max_Prime_Factors(6), 2)
        self.assertEqual(max_Prime_Factors(7), 7)
        self.assertEqual(max_Prime_Factors(8), 2)
        self.assertEqual(max_Prime_Factors(9), 3)

    def test_composite_numbers(self):
        self.assertEqual(max_Prime_Factors(10), 5)
        self.assertEqual(max_Prime_Factors(12), 2)
        self.assertEqual(max_Prime_Factors(14), 2)
        self.assertEqual(max_Prime_Factors(15), 3)
        self.assertEqual(max_Prime_Factors(16), 2)
        self.assertEqual(max_Prime_Factors(18), 2)
        self.assertEqual(max_Prime_Factors(19), 19)
        self.assertEqual(max_Prime_Factors(20), 5)

    def test_large_numbers(self):
        self.assertEqual(max_Prime_Factors(100), 5)
        self.assertEqual(max_Prime_Factors(1000), 2)
        self.assertEqual(max_Prime_Factors(10000), 2)
        self.assertEqual(max_Prime_Factors(100000), 2)
        self.assertEqual(max_Prime_Factors(1000000), 2)
