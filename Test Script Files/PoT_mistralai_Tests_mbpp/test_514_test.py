import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)
        self.assertEqual(sum_elements((0, 0, 0)), 0)
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_elements([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_elements((1,)), 1)
        self.assertEqual(sum_elements((-1,)), -1)

    def test_corner_case_negative_numbers_and_positive(self):
        self.assertEqual(sum_elements((1, -1)), 0)
        self.assertEqual(sum_elements((1, -1, 2)), 2)
        self.assertEqual(sum_elements((-1, 1, -1)), 0)
