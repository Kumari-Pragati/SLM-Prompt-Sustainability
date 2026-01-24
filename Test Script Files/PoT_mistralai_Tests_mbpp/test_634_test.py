import unittest
from mbpp_634_code import range
from six.moves import xrange

class TestEvenPowerSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_Power_Sum(1), 1)
        self.assertEqual(even_Power_Sum(2), 8)
        self.assertEqual(even_Power_Sum(3), 28)
        self.assertEqual(even_Power_Sum(4), 64)
        self.assertEqual(even_Power_Sum(5), 128)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(1000000), 16777216)
        self.assertEqual(even_Power_Sum(1000001), None)
