import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(even_Power_Sum(1), 1)
        self.assertEqual(even_Power_Sum(2), 8)
        self.assertEqual(even_Power_Sum(3), 28)
        self.assertEqual(even_Power_Sum(4), 64)

    def test_edge_and_boundary(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(5), 125)
        self.assertEqual(even_Power_Sum(6), 244)
        self.assertEqual(even_Power_Sum(7), 512)
        self.assertEqual(even_Power_Sum(8), 896)

    def test_complex(self):
        self.assertEqual(even_Power_Sum(9), 1728)
        self.assertEqual(even_Power_Sum(10), 32768)
        self.assertEqual(even_Power_Sum(11), 65536)
        self.assertEqual(even_Power_Sum(12), 122880)
        self.assertEqual(even_Power_Sum(13), 245760)
