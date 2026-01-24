import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):
    def test_typical_input(self):
        lst = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 2, 3, 3), ('b', 4, 5, 6, 3), ('c', 7, 8, 9, 3)])

    def test_edge_case_empty_list(self):
        lst = []
        self.assertEqual(sort_on_occurence(lst), [])

    def test_edge_case_single_element_list(self):
        lst = [('a', [1, 2, 3])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 2, 3, 3)])

    def test_edge_case_single_element_list_empty_sublist(self):
        lst = [('a', [])]
        self.assertEqual(sort_on_occurence(lst), [('a', 0, [], 0)])

    def test_edge_case_single_element_list_single_element_sublist(self):
        lst = [('a', [1])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 1, 1, 1)])

    def test_edge_case_single_element_list_multiple_element_sublist(self):
        lst = [('a', [1, 2, 3])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 2, 3, 3)])

    def test_edge_case_multiple_element_list(self):
        lst = [('a', [1, 2, 3]), ('b', [4, 5, 6])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 2, 3, 3), ('b', 4, 5, 6, 3)])

    def test_edge_case_multiple_element_list_empty_sublist(self):
        lst = [('a', [1, 2, 3]), ('b', [])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 2, 3, 3), ('b', 0, [], 0)])

    def test_edge_case_multiple_element_list_single_element_sublist(self):
        lst = [('a', [1, 2, 3]), ('b', [4])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 2, 3, 3), ('b', 4, 4, 1, 1)])

    def test_edge_case_multiple_element_list_multiple_element_sublist(self):
        lst = [('a', [1, 2, 3]), ('b', [4, 5, 6])]
        self.assertEqual(sort_on_occurence(lst), [('a', 1, 2, 3, 3), ('b', 4, 5, 6, 3)])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_on_occurence('not a list')

    def test_invalid_input_non_list_sublist(self):
        with self.assertRaises(TypeError):
            sort_on_occurence([('a', 'not a list')])

    def test_invalid_input_non_list_sublist_multiple(self):
        with self.assertRaises(TypeError):
            sort_on_occurence([('a', [1, 'not a list']), ('b', [4, 5, 6])])
