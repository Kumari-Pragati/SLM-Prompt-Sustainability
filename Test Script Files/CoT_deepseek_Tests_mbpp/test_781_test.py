import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Divisors(10), "Odd")
        self.assertEqual(count_Divisors(28), "Even")

    def test_edge_cases(self):
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(0), "Even")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Divisors("string")
        with self.assertRaises(ValueError):
            count_Divisors(-10)
