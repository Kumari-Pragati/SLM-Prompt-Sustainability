import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):

    def test_divisor_simple(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(3), 2)
        self.assertEqual(divisor(4), 3)
        self.assertEqual(divisor(5), 2)

    def test_divisor_edge(self):
        self.assertEqual(divisor(0), 1)
        self.assertEqual(divisor(-1), 0)

    def test_divisor_boundary(self):
        self.assertEqual(divisor(100), 9)
        self.assertEqual(divisor(997), 2)

    def test_divisor_complex(self):
        self.assertEqual(divisor(1000), 12)
        self.assertEqual(divisor(9973), 2)
