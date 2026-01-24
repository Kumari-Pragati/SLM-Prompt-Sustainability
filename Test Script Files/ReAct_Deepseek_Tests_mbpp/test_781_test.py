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
        self.assertEqual(count_Divisors(2), "Even")
        self.assertEqual(count_Divisors(3), "Odd")
        self.assertEqual(count_Divisors(4), "Even")

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(count_Divisors(-1), "Odd")
        self.assertEqual(count_Divisors(-4), "Even")
        self.assertEqual(count_Divisors(-9), "Odd")
        self.assertEqual(count_Divisors(-16), "Even")
        self.assertEqual(count_Divisors(-25), "Odd")
