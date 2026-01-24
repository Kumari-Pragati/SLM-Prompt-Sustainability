import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(count_Primes_nums(2), 0)
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(5), 1)
        self.assertEqual(count_Primes_nums(10), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(20), 8)
        self.assertEqual(count_Primes_nums(100), 25)
        self.assertEqual(count_Primes_nums(256), 64)

    def test_complex_and_corner_cases(self):
        self.assertEqual(count_Primes_nums(4), 1)
        self.assertEqual(count_Primes_nums(7), 2)
        self.assertEqual(count_Primes_nums(17), 3)
        self.assertEqual(count_Primes_nums(29), 1)
        self.assertEqual(count_Primes_nums(37), 1)
        self.assertEqual(count_Primes_nums(41), 1)
        self.assertEqual(count_Primes_nums(43), 1)
        self.assertEqual(count_Primes_nums(47), 1)
        self.assertEqual(count_Primes_nums(53), 1)
        self.assertEqual(count_Primes_nums(59), 1)
        self.assertEqual(count_Primes_nums(61), 1)
        self.assertEqual(count_Primes_nums(67), 1)
        self.assertEqual(count_Primes_nums(71), 1)
        self.assertEqual(count_Primes_nums(73), 1)
        self.assertEqual(count_Primes_nums(79), 1)
        self.assertEqual(count_Primes_nums(83), 1)
        self.assertEqual(count_Primes_nums(89), 1)
        self.assertEqual(count_Primes_nums(97), 1)
