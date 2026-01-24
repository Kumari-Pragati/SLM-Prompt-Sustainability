import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_Power_Sum(1), 16)

    def test_boundary_case(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_edge_case(self):
        self.assertEqual(even_Power_Sum(2), 144)

    def test_large_number(self):
        self.assertGreater(even_Power_Sum(10), 10**16)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            even_Power_Sum(-1)
