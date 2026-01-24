import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(20), 8)

    def test_edge_cases(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(4), 2)
        self.assertEqual(count_Primes_nums(5), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Primes_nums("10")
        with self.assertRaises(TypeError):
            count_Primes_nums(None)
        with self.assertRaises(TypeError):
            count_Primes_nums([])
