import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(divisor(4), 3)
        self.assertEqual(divisor(6), 2)
        self.assertEqual(divisor(24), 6)

    def test_edge_input(self):
        self.assertEqual(divisor(0), 0)
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 1)

    def test_boundary_input(self):
        self.assertEqual(divisor(31), 8)
        self.assertEqual(divisor(100), 25)
        self.assertEqual(divisor(1000), 418)

    def test_negative_input(self):
        self.assertEqual(divisor(-1), 0)

    def test_fractional_input(self):
        self.assertEqual(divisor(0.5), 0)
