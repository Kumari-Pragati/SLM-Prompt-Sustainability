import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):

    def test_typical_case(self):
        lst = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
        expected_output = [('a', 1, 3), ('b', 2, 4)]
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_empty_list(self):
        lst = []
        expected_output = []
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_single_element(self):
        lst = [('a', 1)]
        expected_output = [('a', 1, 1)]
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_duplicate_elements(self):
        lst = [('a', 1), ('a', 2), ('a', 3)]
        expected_output = [('a', 1, 3)]
        self.assertEqual(sort_on_occurence(lst), expected_output)

    def test_invalid_input(self):
        lst = [(1, 'a'), ('b', 2), (1, 'c'), ('b', 4)]
        with self.assertRaises(TypeError):
            sort_on_occurence(lst)
