import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_simple_even_powers(self):
        self.assertEqual(even_Power_Sum(2), 256)
        self.assertEqual(even_Power_Sum(4), 1684)
        self.assertEqual(even_Power_Sum(6), 65536)

    def test_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(1), 1)
        self.assertEqual(even_Power_Sum(5), 512)

    def test_complex_and_boundary(self):
        self.assertEqual(even_Power_Sum(10), 1048576)
        self.assertEqual(even_Power_Sum(100), 107374182400)
        self.assertEqual(even_Power_Sum(1000), 1080101974608000)
