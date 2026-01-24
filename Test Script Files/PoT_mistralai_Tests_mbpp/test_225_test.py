import unittest
from mbpp_225_code import find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Min([3, 5, 1, 2, 4], 0, 4), 1)
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)
        self.assertEqual(find_Min([10, 20, 30, 40, 50], 0, 4), 10)

    def test_edge_case_empty_list(self):
        self.assertIsNone(find_Min([], 0, 0))

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min([1], 0, 0), 1)

    def test_edge_case_single_element_end(self):
        self.assertEqual(find_Min([1], 0, 1), 1)

    def test_edge_case_duplicate_end(self):
        self.assertEqual(find_Min([1, 1], 0, 1), 1)

    def test_edge_case_duplicate_middle(self):
        self.assertEqual(find_Min([1, 1, 2], 0, 2), 1)

    def test_edge_case_decreasing(self):
        self.assertEqual(find_Min([5, 4, 3, 2, 1], 0, 4), 1)

    def test_edge_case_increasing(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 1)

    def test_edge_case_increasing_reverse(self):
        self.assertEqual(find_Min([5, 4, 3, 2, 1], 4, 0), 1)
