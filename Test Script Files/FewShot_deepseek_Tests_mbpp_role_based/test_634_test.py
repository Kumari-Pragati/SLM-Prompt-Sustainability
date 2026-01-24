import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 16 + 256)
        self.assertEqual(even_Power_Sum(3), 16 + 256 + 4096)

    def test_boundary_conditions(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(100), sum([(2*i)**8 for i in range(1, 101)]))

    def test_edge_conditions(self):
        self.assertEqual(even_Power_Sum(-1), 0)
        self.assertEqual(even_Power_Sum(1000), sum([(2*i)**8 for i in range(1, 1001)]))
