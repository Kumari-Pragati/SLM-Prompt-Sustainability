import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[5, 3, 2], [8, 1, 6], [4, 7, 9]]
        expected_output = [[2, 3, 5], [1, 6, 8], [4, 7, 9]]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_empty_sublists(self):
        list1 = [ [], [], [] ]
        expected_output = [ [], [], [] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_single_element_sublists(self):
        list1 = [ [5], [8], [4] ]
        expected_output = [ [5], [8], [4] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_duplicate_elements(self):
        list1 = [ [5, 5, 5], [8, 8, 8], [4, 4, 4] ]
        expected_output = [ [5, 5, 5], [8, 8, 8], [4, 4, 4] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_negative_numbers(self):
        list1 = [ [-5, -3, -2], [-8, -1, -6], [-4, -7, -9] ]
        expected_output = [ [-9, -8, -7, -6, -5, -4, -3, -2, -1] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_empty_list(self):
        list1 = []
        expected_output = []
        self.assertEqual(sort_sublists(list1), expected_output)
