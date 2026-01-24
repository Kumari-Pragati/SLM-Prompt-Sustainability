import unittest
from mbpp_453_code import sumofFactors

class TestSumOfFactors(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sumofFactors(6), 31)
        self.assertEqual(sumofFactors(28), 233)
        self.assertEqual(sumofFactors(44), 1375)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sumofFactors(0), 0)
        self.assertEqual(sumofFactors(1), 0)
        self.assertEqual(sumofFactors(2), 1)
        self.assertEqual(sumofFactors(3), 0)
        self.assertEqual(sumofFactors(4), 5)
        self.assertEqual(sumofFactors(5), 6)
        self.assertEqual(sumofFactors(65536), 131072)  # square number
        self.assertEqual(sumofFactors(65537), 65537)  # prime number
        self.assertEqual(sumofFactors(123456), 2857149)  # composite number

    def test_special_case(self):
        self.assertEqual(sumofFactors(4), 5)
        self.assertEqual(sumofFactors(8), 15)
        self.assertEqual(sumofFactors(16), 31)
        self.assertEqual(sumofFactors(32), 63)
