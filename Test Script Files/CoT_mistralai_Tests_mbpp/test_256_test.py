import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_Primes_nums(0), 0)

    def test_single_number(self):
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(5), 1)

    def test_small_numbers(self):
        self.assertEqual(count_Primes_nums(4), 0)
        self.assertEqual(count_Primes_nums(6), 0)
        self.assertEqual(count_Primes_nums(7), 1)
        self.assertEqual(count_Primes_nums(8), 0)
        self.assertEqual(count_Primes_nums(9), 0)

    def test_medium_numbers(self):
        self.assertEqual(count_Primes_nums(10), 2)
        self.assertEqual(count_Primes_nums(11), 1)
        self.assertEqual(count_Primes_nums(12), 0)
        self.assertEqual(count_Primes_nums(13), 1)
        self.assertEqual(count_Primes_nums(14), 0)
        self.assertEqual(count_Primes_nums(15), 1)
        self.assertEqual(count_Primes_nums(16), 0)
        self.assertEqual(count_Primes_nums(17), 1)
        self.assertEqual(count_Primes_nums(18), 0)
        self.assertEqual(count_Primes_nums(19), 1)
        self.assertEqual(count_Primes_nums(20), 2)

    def test_large_numbers(self):
        self.assertEqual(count_Primes_nums(100), 25)
        self.assertEqual(count_Primes_nums(1000), 168)
        self.assertEqual(count_Primes_nums(10000), 1229)
        self.assertEqual(count_Primes_nums(100000), 9592)
        self.assertEqual(count_Primes_nums(1000000), 57614)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_Primes_nums, 'a')
        self.assertRaises(TypeError, count_Primes_nums, -1)
        self.assertRaises(TypeError, count_Primes_nums, 0.5)
