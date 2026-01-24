import unittest
from mbpp_212_code import fourth_Power_Sum

class TestFourthPowerSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(fourth_Power_Sum(1), 1)
        self.assertEqual(fourth_Power_Sum(2), 90)
        self.assertEqual(fourth_Power_Sum(3), 1050)

    def test_boundary_conditions(self):
        self.assertEqual(fourth_Power_Sum(0), 0)
        self.assertEqual(fourth_Power_Sum(100), 100*100*100*100 + sum(i*i*i*i for i in range(1, 100)))

    def test_edge_cases(self):
        self.assertEqual(fourth_Power_Sum(-1), 0)
        self.assertEqual(fourth_Power_Sum(-10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            fourth_Power_Sum('a')
        with self.assertRaises(TypeError):
            fourth_Power_Sum(None)
