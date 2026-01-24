import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_typical_case(self):
        lst = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
        expected_output = [('a', 1, 2), ('b', 3, 4)]
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_empty_list(self):
        lst = []
        expected_output = []
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_single_element(self):
        lst = [('a', 1)]
        expected_output = [('a', 1)]
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_duplicate_elements(self):
        lst = [('a', 1), ('a', 1)]
        expected_output = [('a', 1, 2)]
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_different_elements(self):
        lst = [('a', 1), ('b', 2), ('c', 3)]
        expected_output = [('a', 1), ('b', 2), ('c', 3)]
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_large_input(self):
        lst = [(str(i%10), i) for i in range(100)]
        expected_output = [(str(i%10), i, i+1) for i in range(10)]
        self.assertEqual(sort_on_occurence(lst), expected_output)
