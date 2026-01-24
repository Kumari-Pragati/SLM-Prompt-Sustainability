import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(divisor(6), 2)
        self.assertEqual(divisor(24), 6)
        self.assertEqual(divisor(4913), 68)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(divisor(0), 0)
        self.assertEqual(divisor(1), 0)
        self.assertEqual(divisor(2), 1)
        self.assertEqual(divisor(3), 1)
        self.assertEqual(divisor(4), 1)
        self.assertEqual(divisor(5), 1)
        self.assertEqual(divisor(10), 4)
        self.assertEqual(divisor(12), 3)
        self.assertEqual(divisor(13), 1)
        self.assertEqual(divisor(14), 2)
        self.assertEqual(divisor(15), 1)
        self.assertEqual(divisor(16), 4)

    def test_special_cases(self):
        self.assertEqual(divisor(128), 8)
        self.assertEqual(divisor(2147483647), 65536)
        self.assertEqual(divisor(2 ** 31 - 1), 2147483646)
        self.assertEqual(divisor(2 ** 64 - 1), 18446744073709551615)
