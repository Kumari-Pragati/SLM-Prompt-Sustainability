import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_list([10, 20, 30]), '[10, 20, 30]')

    def test_edge_case_single_digit(self):
        self.assertEqual(sort_list([1, 2, 3]), '[1, 2, 3]')

    def test_edge_case_same_digit_count(self):
        self.assertEqual(sort_list([10, 2, 3]), '[2, 3, 10]')

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sort_list([-10, -20, -30]), '[-30, -20, -10]')

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(sort_list([10, -20, 30]), '[-20, 10, 30]')

    def test_edge_case_large_numbers(self):
        self.assertEqual(sort_list([1000, 2000, 3000]), '[1000, 2000, 3000]')
