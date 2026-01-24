import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Divisors(10), "Odd")

    def test_edge_case(self):
        self.assertEqual(count_Divisors(1), "Even")

    def test_boundary_case(self):
        self.assertEqual(count_Divisors(0), "Even")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Divisors(-10)

    def test_large_number(self):
        self.assertEqual(count_Divisors(10000), "Odd")
