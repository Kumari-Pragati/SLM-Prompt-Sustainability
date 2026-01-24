import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativenum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_single_positive(self):
        self.assertEqual(sum_negativenum([1]), 0)

    def test_single_negative(self):
        self.assertEqual(sum_negativenum([-1]), -1)

    def test_multiple_positive(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_multiple_negative(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_mixed(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4]), -3)

    def test_edge_case_zero(self):
        self.assertEqual(sum_negativenum([0, -1]), -1)

    def test_edge_case_all_positive(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4]), 0)

    def test_edge_case_all_negative(self):
        self.assertEqual(sum_negativenum([-1, -2, -3, -4]), -10)
