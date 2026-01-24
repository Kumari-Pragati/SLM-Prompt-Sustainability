import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_count_Primes_nums(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(20), 8)
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)
        self.assertEqual(count_Primes_nums(3), 2)
        self.assertEqual(count_Primes_nums(17), 7)
