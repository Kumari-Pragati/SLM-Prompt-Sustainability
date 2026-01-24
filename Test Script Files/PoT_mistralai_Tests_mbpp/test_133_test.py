import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_negativenum([-1, 0, 3, -4, 5]), -5)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_edge_case_all_negative(self):
        self.assertEqual(sum_negativenum([-10, -20, -30]), -60)

    def test_edge_case_all_positive(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_boundary_case_zero(self):
        self.assertEqual(sum_negativenum([0]), 0)
