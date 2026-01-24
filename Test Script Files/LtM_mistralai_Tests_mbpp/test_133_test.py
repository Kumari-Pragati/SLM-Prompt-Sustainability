import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_simple_negative(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_single_negative(self):
        self.assertEqual(sum_negativenum([0, -1]), -1)

    def test_edge_zero(self):
        self.assertEqual(sum_negativenum([0]), 0)

    def test_edge_min_int(self):
        self.assertEqual(sum_negativenum([-50, -49, -48]), -147)

    def test_edge_max_int(self):
        self.assertEqual(sum_negativenum([-2147483647, -1, 0]), -2147483647)

    def test_complex_mixed(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4, 5, -6]), -11)
