import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertRaises(ValueError, smallest_num, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(smallest_num([1]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(smallest_num([-5, -3, -1]), -5)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(smallest_num([5, 3, 1]), 1)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(smallest_num([5, 3, -1]), -1)

    def test_edge_case_duplicates(self):
        self.assertEqual(smallest_num([5, 3, 3, 1]), 1)

    def test_edge_case_duplicates_negative(self):
        self.assertEqual(smallest_num([-5, -3, -3, -1]), -5)
