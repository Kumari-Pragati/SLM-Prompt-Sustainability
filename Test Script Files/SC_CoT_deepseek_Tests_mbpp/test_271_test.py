import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_Power_Sum(1), 2^5)

    def test_boundary_case(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_edge_case(self):
        self.assertEqual(even_Power_Sum(2), 2^5 + 4^5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')

        with self.assertRaises(ValueError):
            even_Power_Sum(-1)
