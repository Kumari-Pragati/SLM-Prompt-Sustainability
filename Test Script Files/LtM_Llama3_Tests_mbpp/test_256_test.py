import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(count_Primes_nums(0), 0)

    def test_one(self):
        self.assertEqual(count_Primes_nums(1), 0)

    def test_two(self):
        self.assertEqual(count_Primes_nums(2), 1)

    def test_three(self):
        self.assertEqual(count_Primes_nums(3), 2)

    def test_four(self):
        self.assertEqual(count_Primes_nums(4), 2)

    def test_five(self):
        self.assertEqual(count_Primes_nums(5), 3)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            count_Primes_nums(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            count_Primes_nums('a')

    def test_edge_case_zero_negative(self):
        with self.assertRaises(ValueError):
            count_Primes_nums(0)

    def test_edge_case_zero_positive(self):
        with self.assertRaises(ValueError):
            count_Primes_nums(0)

    def test_edge_case_max(self):
        self.assertEqual(count_Primes_nums(1000), 168)

    def test_edge_case_max_negative(self):
        with self.assertRaises(ValueError):
            count_Primes_nums(-1000)

    def test_edge_case_max_non_integer(self):
        with self.assertRaises(TypeError):
            count_Primes_nums('1000')

    def test_edge_case_max_zero(self):
        with self.assertRaises(ValueError):
            count_Primes_nums(0)
