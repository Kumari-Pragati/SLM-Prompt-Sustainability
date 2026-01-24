import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Sum(10), 12)

    def test_edge_condition(self):
        self.assertEqual(Sum(2), 2)

    def test_boundary_condition(self):
        self.assertEqual(Sum(1), 0)

    def test_zero(self):
        self.assertEqual(Sum(0), 0)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            Sum(-10)

    def test_non_integer(self):
        with self.assertRaises(Exception):
            Sum(10.5)

    def test_large_number(self):
        self.assertEqual(Sum(1000), 5626)
