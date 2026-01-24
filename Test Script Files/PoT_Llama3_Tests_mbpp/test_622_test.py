import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_edge_case_equal_length(self):
        self.assertEqual(get_median([1, 2, 3], [2, 3, 4], 3), 2.5)

    def test_edge_case_one_array_empty(self):
        self.assertEqual(get_median([1, 2, 3], [], 3), 2)

    def test_edge_case_other_array_empty(self):
        self.assertEqual(get_median([], [2, 3, 4], 3), 2.5)

    def test_edge_case_one_array_single_element(self):
        self.assertEqual(get_median([1], [2, 3, 4], 3), 1.5)

    def test_edge_case_other_array_single_element(self):
        self.assertEqual(get_median([1, 2, 3], [4], 3), 2.5)

    def test_edge_case_n_is_zero(self):
        self.assertEqual(get_median([1, 2, 3], [2, 3, 4], 0), 0)

    def test_edge_case_n_is_one(self):
        self.assertEqual(get_median([1], [2, 3, 4], 1), 1)
