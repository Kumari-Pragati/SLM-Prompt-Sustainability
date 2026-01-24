import unittest
from mbpp_453_code import sumofFactors

class TestSumofFactors(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sumofFactors(12), 28)

    def test_edge_case(self):
        self.assertEqual(sumofFactors(1), 1)
        self.assertEqual(sumofFactors(2), 3)

    def test_edge_case2(self):
        self.assertEqual(sumofFactors(3), 4)
        self.assertEqual(sumofFactors(4), 3)

    def test_edge_case3(self):
        self.assertEqual(sumofFactors(5), 6)
        self.assertEqual(sumofFactors(6), 12)

    def test_edge_case4(self):
        self.assertEqual(sumofFactors(7), 8)
        self.assertEqual(sumofFactors(8), 15)

    def test_edge_case5(self):
        self.assertEqual(sumofFactors(9), 13)
        self.assertEqual(sumofFactors(10), 18)

    def test_edge_case6(self):
        self.assertEqual(sumofFactors(11), 12)
        self.assertEqual(sumofFactors(12), 28)

    def test_edge_case7(self):
        self.assertEqual(sumofFactors(13), 14)
        self.assertEqual(sumofFactors(14), 24)

    def test_edge_case8(self):
        self.assertEqual(sumofFactors(15), 24)
        self.assertEqual(sumofFactors(16), 31)

    def test_edge_case9(self):
        self.assertEqual(sumofFactors(17), 18)
        self.assertEqual(sumofFactors(18), 39)

    def test_edge_case10(self):
        self.assertEqual(sumofFactors(19), 20)
        self.assertEqual(sumofFactors(20), 42)
