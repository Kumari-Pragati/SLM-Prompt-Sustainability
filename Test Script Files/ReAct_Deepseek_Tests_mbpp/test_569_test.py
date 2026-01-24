import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_empty_sublists(self):
        list1 = [ [], [] ]
        expected_output = [ [], [] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_single_element_sublists(self):
        list1 = [ [3], [2], [1] ]
        expected_output = [ [1], [2], [3] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_duplicate_elements(self):
        list1 = [ [3, 2, 2, 1], [6, 5, 5, 4], [9, 8, 8, 7] ]
        expected_output = [ [1, 2, 2, 3], [4, 5, 5, 6], [7, 8, 8, 9] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_empty_main_list(self):
        list1 = []
        expected_output = []
        self.assertEqual(sort_sublists(list1), expected_output)
