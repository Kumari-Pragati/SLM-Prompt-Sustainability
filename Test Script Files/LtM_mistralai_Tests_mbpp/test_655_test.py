import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 256)
        self.assertEqual(fifth_Power_Sum(3), 19683)

    def test_edge_cases(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(1000), 10000000000000)

    def test_complex_cases(self):
        self.assertEqual(fifth_Power_Sum(10), 1000000000)
        self.assertEqual(fifth_Power_Sum(20), 2000000000000)
        self.assertEqual(fifth_Power_Sum(30), 300000000000000)
