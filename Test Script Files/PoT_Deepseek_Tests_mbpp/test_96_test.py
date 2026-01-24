import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(4), 3)
        self.assertEqual(divisor(10), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(divisor(0), 1)
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(100), 9)

    def test_corner_cases(self):
        self.assertEqual(divisor(97), 2)
        self.assertEqual(divisor(96), 9)
        self.assertEqual(divisor(95), 2)
