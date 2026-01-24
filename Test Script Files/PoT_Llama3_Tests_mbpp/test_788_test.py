import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(new_tuple([1, 2, 3], 'a'), ('1', '2', '3', 'a'))

    def test_empty_list(self):
        self.assertEqual(new_tuple([], 'a'), ('a',))

    def test_single_element_list(self):
        self.assertEqual(new_tuple([1], 'a'), ('1', 'a'))

    def test_edge_case_empty_string(self):
        self.assertEqual(new_tuple([1, 2, 3], ''), ('1', '2', '3', ''))

    def test_edge_case_single_element_string(self):
        self.assertEqual(new_tuple([1, 2, 3], 'a'), ('1', '2', '3', 'a'))

    def test_edge_case_list_of_strings(self):
        self.assertEqual(new_tuple(['a', 'b', 'c'], 'd'), ('a', 'b', 'c', 'd'))

    def test_edge_case_list_of_integers(self):
        self.assertEqual(new_tuple([1, 2, 3], 'a'), ('1', '2', '3', 'a'))

    def test_edge_case_list_of_mixed_types(self):
        self.assertEqual(new_tuple([1, 'a', 2.5], 'b'), ('1', 'a', '2.5', 'b'))
