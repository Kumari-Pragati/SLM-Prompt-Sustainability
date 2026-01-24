import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(fourth_Power_Sum(4), 385)

    def test_boundary_condition(self):
        self.assertEqual(fourth_Power_Sum(1), 1)

    def test_edge_condition(self):
        self.assertEqual(fourth_Power_Sum(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            fourth_Power_Sum(-1)
