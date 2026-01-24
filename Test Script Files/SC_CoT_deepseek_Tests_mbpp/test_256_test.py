import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_edge_case(self):
        self.assertEqual(count_Primes_nums(2), 1)

    def test_boundary_case(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Primes_nums(-10)
        with self.assertRaises(TypeError):
            count_Primes_nums('abc')
