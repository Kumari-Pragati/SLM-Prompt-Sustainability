import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 64)
        self.assertEqual(even_Power_Sum(3), 144)
        self.assertEqual(even_Power_Sum(4), 256)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(5), 400)
        self.assertEqual(even_Power_Sum(10), 3200)
        self.assertEqual(even_Power_Sum(20), 12800)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(TypeError):
            even_Power_Sum(None)
