import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(even_Power_Sum(5), 5760)

    def test_edge_case(self):
        self.assertEqual(even_Power_Sum(1), 32)
        self.assertEqual(even_Power_Sum(2), 128)

    def test_boundary_case(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(3), 2880)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
