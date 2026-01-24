import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(count_Divisors(4), "Even")
        self.assertEqual(count_Divisors(6), "Even")
        self.assertEqual(count_Divisors(25), "Odd")
        self.assertEqual(count_Divisors(28), "Even")

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(2), "Even")
        self.assertEqual(count_Divisors(3), "Odd")
        self.assertEqual(count_Divisors(49), "Odd")
        self.assertEqual(count_Divisors(50), "Even")
        self.assertEqual(count_Divisors(100), "Even")
        self.assertEqual(count_Divisors(121), "Odd")

    def test_corner_cases(self):
        self.assertEqual(count_Divisors(0), "Odd")
        self.assertEqual(count_Divisors(1024), "Even")
        self.assertEqual(count_Divisors(2 ** 31 - 1), "Odd")
        self.assertEqual(count_Divisors(2 ** 31), "Even")
