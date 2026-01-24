import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sumofFactors(1), 1)
        self.assertEqual(sumofFactors(2), 3)
        self.assertEqual(sumofFactors(3), 4)
        self.assertEqual(sumofFactors(4), 7)
        self.assertEqual(sumofFactors(5), 6)
        self.assertEqual(sumofFactors(6), 12)
        self.assertEqual(sumofFactors(7), 8)
        self.assertEqual(sumofFactors(8), 15)
        self.assertEqual(sumofFactors(9), 13)
        self.assertEqual(sumofFactors(10), 18)

    def test_edge(self):
        self.assertEqual(sumofFactors(0), 1)
        self.assertEqual(sumofFactors(11), 12)
        self.assertEqual(sumofFactors(12), 28)
        self.assertEqual(sumofFactors(13), 14)
        self.assertEqual(sumofFactors(14), 24)
        self.assertEqual(sumofFactors(15), 24)
        self.assertEqual(sumofFactors(16), 33)
        self.assertEqual(sumofFactors(17), 18)
        self.assertEqual(sumofFactors(18), 39)
        self.assertEqual(sumofFactors(19), 20)

    def test_complex(self):
        self.assertEqual(sumofFactors(20), 42)
        self.assertEqual(sumofFactors(21), 44)
        self.assertEqual(sumofFactors(22), 48)
        self.assertEqual(sumofFactors(23), 24)
        self.assertEqual(sumofFactors(24), 60)
        self.assertEqual(sumofFactors(25), 52)
        self.assertEqual(sumofFactors(26), 54)
        self.assertEqual(sumofFactors(27), 56)
        self.assertEqual(sumofFactors(28), 60)
        self.assertEqual(sumofFactors(29), 60)
