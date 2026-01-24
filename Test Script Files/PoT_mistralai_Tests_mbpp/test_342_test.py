import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_minimum_range([[1, 3, 5], [2, 4, 6], [7, 8, 9]]), (1, 9))
        self.assertEqual(find_minimum_range([[10, 20, 30], [40, 50, 60], [70, 80, 90]])), (10, 90)

    def test_edge_case_empty_list(self):
        self.assertIsNone(find_minimum_range([]))

    def test_edge_case_single_list(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))

    def test_edge_case_single_element(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))
        self.assertEqual(find_minimum_range([[1], [2]]), (1, 2))

    def test_corner_case_decreasing_sequence(self):
        self.assertEqual(find_minimum_range([[10, 9, 8], [7, 6, 5], [4, 3, 2]]), (10, 2))

    def test_corner_case_increasing_sequence(self):
        self.assertEqual(find_minimum_range([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (1, 9))
