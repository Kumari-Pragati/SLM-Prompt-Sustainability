import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(even_Power_Sum(5), 5760)

    def test_edge_case(self):
        self.assertEqual(even_Power_Sum(1), 0)
        self.assertEqual(even_Power_Sum(2), 32)

    def test_boundary_case(self):
        self.assertEqual(even_Power_Sum(3), 576)
        self.assertEqual(even_Power_Sum(4), 5760)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
