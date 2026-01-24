import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_Of_Primes(10), 2 + 3 + 5 + 7)
        self.assertEqual(sum_Of_Primes(20), 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19)
        self.assertEqual(sum_Of_Primes(100), 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 + 31 + 37 + 41 + 43 + 47 + 53 + 59 + 61 + 67 + 71 + 73 + 79 + 83 + 89 + 97)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(1), 1)
        self.assertEqual(sum_Of_Primes(2), 2)
        self.assertEqual(sum_Of_Primes(3), 3)
        self.assertEqual(sum_Of_Primes(4), 2)
        self.assertEqual(sum_Of_Primes(5), 2 + 3)

    def test_large_numbers(self):
        self.assertEqual(sum_Of_Primes(100000), expected=sum(range(2, 100001)) - sum(primes))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sum_Of_Primes, "not_a_number")
        self.assertRaises(TypeError, sum_Of_Primes, -1)
        self.assertRaises(TypeError, sum_Of_Primes, float("inf"))
