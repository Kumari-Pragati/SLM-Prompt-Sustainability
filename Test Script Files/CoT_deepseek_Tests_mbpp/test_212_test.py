import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(fourth_Power_Sum(4), 385)

    def test_boundary_conditions(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(1), 1)

    def test_edge_cases(self):
        self.assertEqual(fourth_Power_Sum(-1), 0)
        self.assertEqual(fourth_Power_Sum(2), 25)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum('a')
        with self.assertRaises(TypeError):
            fourth_Power_Sum(None)
        with self.assertRaises(TypeError):
            fourth_Power_Sum([])
