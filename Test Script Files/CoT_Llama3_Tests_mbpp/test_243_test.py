import unittest
from mbpp_243_code import sort_on_occurence

class TestSortOnOccurence(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3], [1, 2, 3], [4, 5, 6]]), 
                         [(1, 2, 3, 2), (4, 5, 6, 1)])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_on_occurence([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3]]), [(1, 2, 3, 1)])

    def test_edge_case_single_element_dict(self):
        self.assertEqual(sort_on_occurence([[1, 2, 3]]), [(1, 2, 3, 1)])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_on_occurence('abc')

    def test_invalid_input_non_list_of_lists(self):
        with self.assertRaises(TypeError):
            sort_on_occurence([1, 2, 3])
