import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(count_Primes_nums(0), 0)

    def test_one_input(self):
        self.assertEqual(count_Primes_nums(1), 0)

    def test_small_prime_input(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_large_prime_input(self):
        self.assertEqual(count_Primes_nums(100), 25)

    def test_non_prime_input(self):
        self.assertEqual(count_Primes_nums(20), 4)

    def test_edge_case_input(self):
        self.assertEqual(count_Primes_nums(2), 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Primes_nums("a")

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            count_Primes_nums(-1)
