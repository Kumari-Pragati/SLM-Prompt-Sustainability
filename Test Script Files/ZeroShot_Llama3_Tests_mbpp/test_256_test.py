import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_count_primes_nums(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(5), 2)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(2), 1)
        self.assertEqual(count_Primes_nums(3), 2)
        self.assertEqual(count_Primes_nums(4), 2)
        self.assertEqual(count_Primes_nums(6), 3)
        self.assertEqual(count_Primes_nums(7), 4)
        self.assertEqual(count_Primes_nums(8), 4)
        self.assertEqual(count_Primes_nums(9), 4)

    def test_count_primes_nums_edge_cases(self):
        self.assertEqual(count_Primes_nums(-1), 0)
        self.assertEqual(count_Primes_nums(-5), 0)
        self.assertEqual(count_Primes_nums(-10), 0)
