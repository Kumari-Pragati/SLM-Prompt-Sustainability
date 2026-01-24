import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(2), "Even")
        self.assertEqual(count_Divisors(4), "Odd")
        self.assertEqual(count_Divisors(9), "Even")

    def test_edge_conditions(self):
        self.assertEqual(count_Divisors(0), "Even")
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(2), "Even")

    def test_complex_cases(self):
        self.assertEqual(count_Divisors(100), "Even")
        self.assertEqual(count_Divisors(101), "Odd")
        self.assertEqual(count_Divisors(1000), "Even")
