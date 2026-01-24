import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(20), 8)

    def test_edge_conditions(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(100), 25)
        self.assertEqual(count_Primes_nums(1000), 168)

    def test_complex_cases(self):
        self.assertEqual(count_Primes_nums(10000), 1229)
