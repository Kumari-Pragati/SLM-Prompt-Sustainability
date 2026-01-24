import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 134)
        self.assertEqual(fifth_Power_Sum(3), 1440)

    def test_edge_conditions(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(-1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(fifth_Power_Sum(10), 20511780)
        self.assertEqual(fifth_Power_Sum(100), 3355033600)

    def test_complex_cases(self):
        self.assertEqual(fifth_Power_Sum(1000), 1188257568000)
