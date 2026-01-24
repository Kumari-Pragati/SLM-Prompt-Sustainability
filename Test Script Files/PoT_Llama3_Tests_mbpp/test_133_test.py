import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativenum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_negativenum([-1, 2, 3, -4, 5]), -6)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(sum_negativenum([-1]), -1)

    def test_edge_case_single_positive(self):
        self.assertEqual(sum_negativenum([1]), 0)

    def test_edge_case_all_positive(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)

    def test_edge_case_all_negative(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)

    def test_edge_case_mixed(self):
        self.assertEqual(sum_negativenum([-1, 2, 3, -4, 5, -6]), -6)
