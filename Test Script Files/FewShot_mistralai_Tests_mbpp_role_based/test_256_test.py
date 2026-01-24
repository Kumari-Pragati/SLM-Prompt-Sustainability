import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(20), 8)
        self.assertEqual(count_Primes_nums(100), 25)

    def test_zero(self):
        self.assertEqual(count_Primes_nums(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Primes_nums(-1), 0)
        self.assertEqual(count_Primes_nums(-10), 0)
        self.assertEqual(count_Primes_nums(-100), 0)

    def test_one(self):
        self.assertEqual(count_Primes_nums(1), 0)
