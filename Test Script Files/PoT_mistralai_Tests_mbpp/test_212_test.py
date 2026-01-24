import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 8)
        self.assertEqual(fourth_Power_Sum(3), 27)
        self.assertEqual(fourth_Power_Sum(10), 1024)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(1000), 10000000000)
        self.assertEqual(fourth_Power_Sum(1000000), 10000000000000000000)
