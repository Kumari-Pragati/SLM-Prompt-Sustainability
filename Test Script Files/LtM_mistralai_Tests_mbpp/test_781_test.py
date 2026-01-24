import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_simple_even(self):
        self.assertEqual(count_Divisors(4), "Even")

    def test_simple_odd(self):
        self.assertEqual(count_Divisors(3), "Odd")

    def test_small_even(self):
        self.assertEqual(count_Divisors(6), "Even")

    def test_small_odd(self):
        self.assertEqual(count_Divisors(5), "Odd")

    def test_edge_case_1(self):
        self.assertEqual(count_Divisors(1), "Odd")

    def test_edge_case_2(self.max_value):
        self.assertEqual(count_Divisors(2**31 - 1), "Even")

    def test_edge_case_3(self.min_value):
        self.assertEqual(count_Divisors(1), "Odd")

    def test_complex_case_1(self):
        self.assertEqual(count_Divisors(20), "Even")

    def test_complex_case_2(self):
        self.assertEqual(count_Divisors(28), "Odd")
