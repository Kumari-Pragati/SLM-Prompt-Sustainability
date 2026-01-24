import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_small_positive_number(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_large_positive_number(self):
        self.assertEqual(count_Primes_nums(100), 25)

    def test_zero(self):
        self.assertEqual(count_Primes_nums(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            count_Primes_nums(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            count_Primes_nums(10.5)
