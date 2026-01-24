import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        input_list = [[3, 2, 1], [6, 5, 4]]
        expected_output = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_empty_sublists(self):
        input_list = [ [], [] ]
        expected_output = [ [], [] ]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_single_sublist(self):
        input_list = [ [3, 2, 1] ]
        expected_output = [ [1, 2, 3] ]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_already_sorted_sublists(self):
        input_list = [ [1, 2, 3], [4, 5, 6] ]
        expected_output = [ [1, 2, 3], [4, 5, 6] ]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_single_element_sublists(self):
        input_list = [ [3], [2], [1] ]
        expected_output = [ [1], [2], [3] ]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_negative_numbers(self):
        input_list = [ [-3, -2, -1], [-6, -5, -4] ]
        expected_output = [ [-3, -2, -1], [-6, -5, -4] ]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_mixed_numbers(self):
        input_list = [ [-3, 2, 1], [6, -5, 4] ]
        expected_output = [ [-3, 1, 2], [-5, 4, 6] ]
        self.assertEqual(sort_sublists(input_list), expected_output)

    def test_empty_input(self):
        input_list = []
        expected_output = []
        self.assertEqual(sort_sublists(input_list), expected_output)
