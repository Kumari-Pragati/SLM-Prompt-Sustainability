import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 90)
        self.assertEqual(fourth_Power_Sum(3), 980)

    def test_edge_cases(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(-1), 0)

    def test_boundary_cases(self):
        self.assertEqual(fourth_Power_Sum(100), 100*100*100*100 + 99*99*99*99)
