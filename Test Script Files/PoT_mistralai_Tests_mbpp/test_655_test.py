import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 256)
        self.assertEqual(fifth_Power_Sum(3), 19728)
        self.assertEqual(fifth_Power_Sum(10), 327680)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(1000), 1000000000000)
        self.assertEqual(fifth_Power_Sum(1000000), 1000000000000000000)
