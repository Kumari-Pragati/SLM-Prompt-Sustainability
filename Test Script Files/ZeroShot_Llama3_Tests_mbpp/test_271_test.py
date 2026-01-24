import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_Power_Sum(self):
        self.assertEqual(even_Power_Sum(1), 32)
        self.assertEqual(even_Power_Sum(2), 128)
        self.assertEqual(even_Power_Sum(3), 256)
        self.assertEqual(even_Power_Sum(4), 512)
        self.assertEqual(even_Power_Sum(5), 1024)
        self.assertEqual(even_Power_Sum(6), 2048)
        self.assertEqual(even_Power_Sum(7), 4096)
        self.assertEqual(even_Power_Sum(8), 8192)
        self.assertEqual(even_Power_Sum(9), 16384)
        self.assertEqual(even_Power_Sum(10), 32768)

    def test_even_Power_Sum_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
