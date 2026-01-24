import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_edge_case(self):
        self.assertEqual(count_Primes_nums(2), 0)
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(4), 2)

    def test_boundary_case(self):
        self.assertEqual(count_Primes_nums(5), 2)
        self.assertEqual(count_Primes_nums(6), 2)
        self.assertEqual(count_Primes_nums(7), 3)

    def test_large_input(self):
        self.assertEqual(count_Primes_nums(100), 25)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Primes_nums('a')

    def test_zero_input(self):
        with self.assertRaises(TypeError):
            count_Primes_nums(0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            count_Primes_nums(-1)
