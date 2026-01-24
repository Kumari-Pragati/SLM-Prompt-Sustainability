import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        input_list = [[5, 3], [1, 2, 3], [4, 2]]
        expected_output = [[3, 5], [1, 2, 3], [2, 4]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_empty_sublists(self):
        input_list = [[], []]
        expected_output = [ [], [] ]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_single_sublist(self):
        input_list = [[1, 2, 3]]
        expected_output = [[1, 2, 3]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_duplicate_elements(self):
        input_list = [[3, 2, 1], [2, 2, 2], [1, 2, 3]]
        expected_output = [[1, 2, 3], [2, 2, 2], [1, 2, 3]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_negative_numbers(self):
        input_list = [[-1, -2], [-2, -1]]
        expected_output = [[-2, -1], [-2, -1]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_empty_input(self):
        input_list = []
        expected_output = []
        self.assertEqual(sort_sublists(input_list), expected_output)
