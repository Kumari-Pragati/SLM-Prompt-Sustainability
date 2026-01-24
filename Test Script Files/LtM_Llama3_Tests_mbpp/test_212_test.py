import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 16)
        self.assertEqual(fourth_Power_Sum(3), 81)
        self.assertEqual(fourth_Power_Sum(4), 256)

    def test_edge_cases(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(5), 625)
        self.assertEqual(fourth_Power_Sum(-1), 0)
        self.assertEqual(fourth_Power_Sum(-5), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum("a")
        with self.assertRaises(TypeError):
            fourth_Power_Sum(None)
