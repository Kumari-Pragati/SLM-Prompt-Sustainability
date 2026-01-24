import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(4), "Even")
        self.assertEqual(count_Divisors(9), "Odd")
        self.assertEqual(count_Divisors(16), "Even")
        self.assertEqual(count_Divisors(25), "Odd")

    def test_edge_cases(self):
        self.assertEqual(count_Divisors(0), "Even")
        self.assertEqual(count_Divisors(1), "Odd")

    def test_boundary_cases(self):
        self.assertEqual(count_Divisors(2), "Even")
        self.assertEqual(count_Divisors(3), "Odd")
        self.assertEqual(count_Divisors(5), "Odd")
        self.assertEqual(count_Divisors(7), "Odd")
        self.assertEqual(count_Divisors(8), "Even")
        self.assertEqual(count_Divisors(10), "Even")

    def test_corner_cases(self):
        self.assertEqual(count_Divisors(100), "Even")
        self.assertEqual(count_Divisors(101), "Odd")
        self.assertEqual(count_Divisors(1000), "Even")
        self.assertEqual(count_Divisors(1001), "Odd")
