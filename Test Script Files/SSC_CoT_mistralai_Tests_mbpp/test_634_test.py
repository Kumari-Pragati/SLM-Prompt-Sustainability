import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(even_Power_Sum(4), 64)
        self.assertEqual(even_Power_Sum(16), 1024)

    def test_edge_cases(self):
        self.assertEqual(even_Power_Sum(1), 1)
        self.assertEqual(even_Power_Sum(2), 8)
        self.assertEqual(even_Power_Sum(3), 81)

    def test_boundary(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(2147483647), 2147483647)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, even_Power_Sum, -1)
        self.assertRaises(TypeError, even_Power_Sum, 'not_a_number')
