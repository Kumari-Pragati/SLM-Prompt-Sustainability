import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_even_power_sum(self):
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(2), 32)
        self.assertEqual(even_Power_Sum(3), 1280)
        self.assertEqual(even_Power_Sum(4), 16384)
        self.assertEqual(even_Power_Sum(5), 32768)
        self.assertEqual(even_Power_Sum(10), 1048576)
        self.assertEqual(even_Power_Sum(20), 4294967296)

    def test_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(-1), 0)
        self.assertEqual(even_Power_Sum(-10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(TypeError):
            even_Power_Sum(None)
        with self.assertRaises(TypeError):
            even_Power_Sum(1.5)
