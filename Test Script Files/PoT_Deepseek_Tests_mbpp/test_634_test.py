import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_Power_Sum(1), 2^4)
        self.assertEqual(even_Power_Sum(2), 2^4 + 4^4)
        self.assertEqual(even_Power_Sum(3), 2^4 + 4^4 + 6^4)

    def test_edge_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(even_Power_Sum(100), sum([(2*i)**4 for i in range(1, 101)]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(ValueError):
            even_Power_Sum(-1)
