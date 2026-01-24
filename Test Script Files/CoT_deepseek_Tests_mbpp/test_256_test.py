import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_single_prime(self):
        self.assertEqual(count_Primes_nums(2), 1)

    def test_no_prime(self):
        self.assertEqual(count_Primes_nums(1), 0)

    def test_large_number(self):
        self.assertGreater(count_Primes_nums(1000), 250)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            count_Primes_nums(-10)

    def test_zero(self):
        with self.assertRaises(Exception):
            count_Primes_nums(0)
