import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(even_Power_Sum(4), 1024)
        self.assertEqual(even_Power_Sum(10), 1088)
        self.assertEqual(even_Power_Sum(20), 12288)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(2), 256)
        self.assertEqual(even_Power_Sum(3), 0)
        self.assertEqual(even_Power_Sum(5), 0)
        self.assertEqual(even_Power_Sum(6), 4096)
        self.assertEqual(even_Power_Sum(7), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_Power_Sum(0)
        with self.assertRaises(TypeError):
            even_Power_Sum(-1)
        with self.assertRaises(TypeError):
            even_Power_Sum(3.5)
