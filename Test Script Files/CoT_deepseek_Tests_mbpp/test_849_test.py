import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Sum(10), 12)

    def test_prime_number(self):
        self.assertEqual(Sum(5), 5)

    def test_boundary_conditions(self):
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(1), 0)

    def test_large_number(self):
        self.assertEqual(Sum(100), 120)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            Sum(-10)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            Sum(10.5)

    def test_string_input(self):
        with self.assertRaises(Exception):
            Sum("10")
