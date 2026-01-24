import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(20), 8)
        self.assertEqual(count_Primes_nums(50), 15)

    def test_edge_cases(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)
        self.assertEqual(count_Primes_nums(3), 2)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(count_Primes_nums(-10), 0)
        self.assertEqual(count_Primes_nums(-1), 0)
        self.assertEqual(count_Primes_nums(-2), 0)
        self.assertEqual(count_Primes_nums(-3), 0)
