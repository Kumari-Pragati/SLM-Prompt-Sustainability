import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_edge_conditions(self):
        self.assertEqual(count_range_in_list([], 1, 10), 0)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 1), 1)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 6, 10), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 6), 5)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 0, 1), 1)

    def test_complex_cases(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 2)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 3, 5), 2)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)
