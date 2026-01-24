import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 8)
        self.assertEqual(fourth_Power_Sum(3), 27)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(100000), 10000000000000)

    def test_complex_scenarios(self):
        self.assertEqual(fourth_Power_Sum(10), 197230)
        self.assertEqual(fourth_Power_Sum(100), 1000000000)
        self.assertEqual(fourth_Power_Sum(1000), 10000000000000)
