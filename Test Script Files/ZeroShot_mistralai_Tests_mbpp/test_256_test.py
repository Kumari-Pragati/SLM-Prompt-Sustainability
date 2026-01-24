import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_count_primes_zero(self):
        self.assertEqual(count_Primes_nums(0), 0)

    def test_count_primes_negative(self):
        self.assertEqual(count_Primes_nums(-1), 0)

    def test_count_primes_one(self):
        self.assertEqual(count_Primes_nums(1), 0)

    def test_count_primes_two(self):
        self.assertEqual(count_Primes_nums(2), 1)

    def test_count_primes_small_numbers(self):
        self.assertEqual(count_Primes_nums(5), 2)
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(20), 8)

    def test_count_primes_large_numbers(self):
        self.assertEqual(count_Primes_nums(100), 25)
        self.assertEqual(count_Primes_nums(1000), 168)
        self.assertEqual(count_Primes_nums(10000), 1229)
