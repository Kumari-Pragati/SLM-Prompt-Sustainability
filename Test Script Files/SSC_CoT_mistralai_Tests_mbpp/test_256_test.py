import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_Primes_nums(10), 4)
        self.assertEqual(count_Primes_nums(200), 64)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(4), 1)
        self.assertEqual(count_Primes_nums(5), 1)
        self.assertEqual(count_Primes_nums(6), 0)
        self.assertEqual(count_Primes_nums(7), 1)
        self.assertEqual(count_Primes_nums(8), 0)
        self.assertEqual(count_Primes_nums(9), 0)
        self.assertEqual(count_Primes_nums(1000000), 78498)

    def test_special_cases(self):
        self.assertEqual(count_Primes_nums(2), 1)
        self.assertEqual(count_Primes_nums(3), 1)
        self.assertEqual(count_Primes_nums(5), 1)
        self.assertEqual(count_Primes_nums(7), 1)
        self.assertEqual(count_Primes_nums(11), 1)
        self.assertEqual(count_Primes_nums(13), 1)
        self.assertEqual(count_Primes_nums(17), 1)
        self.assertEqual(count_Primes_nums(19), 1)
        self.assertEqual(count_Primes_nums(23), 1)
        self.assertEqual(count_Primes_nums(29), 1)
        self.assertEqual(count_Primes_nums(31), 1)
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
