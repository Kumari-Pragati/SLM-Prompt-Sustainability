import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(2), 32)
        self.assertEqual(even_Power_Sum(3), 1280)
        self.assertEqual(even_Power_Sum(4), 16384)
        self.assertEqual(even_Power_Sum(5), 32768)

    def test_edge(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(10), 32768)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(TypeError):
            even_Power_Sum(None)
