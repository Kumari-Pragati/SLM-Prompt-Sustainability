import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_edge_case_zero(self):
        self.assertEqual(sum_num([0, 0, 0, 0, 0]), 0.0)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_num([1]), 1.0)

    def test_edge_case_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            sum_num([])

    def test_edge_case_single_zero(self):
        self.assertEqual(sum_num([0]), 0.0)

    def test_edge_case_single_non_zero(self):
        self.assertEqual(sum_num([1]), 1.0)

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(sum_num([0, 0, 0]), 0.0)

    def test_edge_case_multiple_non_zeros(self):
        self.assertEqual(sum_num([1, 2, 3]), 2.0)

    def test_edge_case_mixed_zeros_and_non_zeros(self):
        self.assertEqual(sum_num([0, 1, 2, 0, 3]), 1.2)
