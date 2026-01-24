import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(even_Power_Sum(1), 2**10)
        self.assertEqual(even_Power_Sum(2), 2**10 + 4**10)
        self.assertEqual(even_Power_Sum(3), 2**10 + 4**10 + 6**10)

    def test_boundary_conditions(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(10), sum([(2*i)**10 for i in range(1, 11)]))

    def test_edge_conditions(self):
        self.assertEqual(even_Power_Sum(-1), 0)
        self.assertEqual(even_Power_Sum(11), sum([(2*i)**10 for i in range(1, 11)]) + 12**10)
