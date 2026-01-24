import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(25), 12)
        self.assertEqual(count_Primes_nums(100), 25)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(4), 1)
        self.assertEqual(count_Primes_nums(5), 1)
        self.assertEqual(count_Primes_nums(6), 0)
        self.assertEqual(count_Primes_nums(7), 1)
        self.assertEqual(count_Primes_nums(8), 0)
        self.assertEqual(count_Primes_nums(9), 0)
        self.assertEqual(count_Primes_nums(1000), 168)
        self.assertEqual(count_Primes_nums(10000), 1229)
        self.assertEqual(count_Primes_nums(100000), 9592)
        self.assertEqual(count_Primes_nums(1000000), 57614)
