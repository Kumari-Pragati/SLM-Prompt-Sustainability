import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 90)
        self.assertEqual(fourth_Power_Sum(3), 980)

    def test_edge_conditions(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(10), 0)

    def test_boundary_conditions(self):
        self.assertEqual(fourth_Power_Sum(100), 25502500)
        self.assertEqual(fourth_Power_Sum(1000), 999001000000)

    def test_complex_cases(self):
        self.assertEqual(fourth_Power_Sum(10000), 9999000100000000)
