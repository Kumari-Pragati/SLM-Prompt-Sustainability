import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_in_Range(1, 5), 9)

    def test_edge_case_larger_than_r(self):
        self.assertEqual(sum_in_Range(5, 1), -4)

    def test_edge_case_larger_than_l(self):
        self.assertEqual(sum_in_Range(5, 5), 0)

    def test_edge_case_l_equal_r(self):
        self.assertEqual(sum_in_Range(5, 5), 0)

    def test_edge_case_l_smaller_than_r(self):
        self.assertEqual(sum_in_Range(1, 5), 9)

    def test_edge_case_l_equal_r_negative(self):
        self.assertEqual(sum_in_Range(-5, -5), 0)

    def test_edge_case_r_smaller_than_l(self):
        self.assertEqual(sum_in_Range(5, 1), -4)

    def test_edge_case_l_smaller_than_r_negative(self):
        self.assertEqual(sum_in_Range(-5, -1), 6)
