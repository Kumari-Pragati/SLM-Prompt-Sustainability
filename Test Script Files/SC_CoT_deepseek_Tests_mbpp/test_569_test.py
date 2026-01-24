import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[5, 3, 2], [9, 8, 7], [1, 4, 6]]
        expected_output = [[2, 3, 5], [7, 8, 9], [1, 4, 6]]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_empty_sublists(self):
        list1 = [ [], [], [] ]
        expected_output = [ [], [], [] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_single_element_sublists(self):
        list1 = [ [5], [9], [1] ]
        expected_output = [ [5], [9], [1] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_already_sorted_sublists(self):
        list1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
        expected_output = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
        self.assertEqual(sort_sublists(list1), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_sublists(123)
