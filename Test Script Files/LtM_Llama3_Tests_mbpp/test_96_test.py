import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(3), 2)
        self.assertEqual(divisor(4), 2)
        self.assertEqual(divisor(5), 2)
        self.assertEqual(divisor(6), 2)
        self.assertEqual(divisor(7), 2)
        self.assertEqual(divisor(8), 3)
        self.assertEqual(divisor(9), 3)
        self.assertEqual(divisor(10), 2)

    def test_edge(self):
        self.assertEqual(divisor(0), 0)
        self.assertEqual(divisor(1), 1)
        self.assertEqual(divisor(2), 2)
        self.assertEqual(divisor(3), 2)
        self.assertEqual(divisor(4), 2)
        self.assertEqual(divisor(5), 2)
        self.assertEqual(divisor(6), 2)
        self.assertEqual(divisor(7), 2)
        self.assertEqual(divisor(8), 3)
        self.assertEqual(divisor(9), 3)
        self.assertEqual(divisor(10), 2)

    def test_complex(self):
        self.assertEqual(divisor(11), 2)
        self.assertEqual(divisor(12), 4)
        self.assertEqual(divisor(13), 2)
        self.assertEqual(divisor(14), 3)
        self.assertEqual(divisor(15), 4)
        self.assertEqual(divisor(16), 3)
        self.assertEqual(divisor(17), 2)
        self.assertEqual(divisor(18), 4)
        self.assertEqual(divisor(19), 2)
        self.assertEqual(divisor(20), 2)
