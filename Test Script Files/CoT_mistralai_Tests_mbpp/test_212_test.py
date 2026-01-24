import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 8)
        self.assertEqual(fourth_Power_Sum(3), 33)
        self.assertEqual(fourth_Power_Sum(4), 128)
        self.assertEqual(fourth_Power_Sum(5), 335)

    def test_edge_cases(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(math.inf), math.inf)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, fourth_Power_Sum, "string")
        self.assertRaises(TypeError, fourth_Power_Sum, -1)
        self.assertRaises(TypeError, fourth_Power_Sum, float('nan'))
