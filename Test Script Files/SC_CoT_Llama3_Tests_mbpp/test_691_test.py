import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):
    def test_typical_input(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['c'], 4: ['d'], 5: ['e']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case_single_element_list(self):
        test_list = [(1, 'a')]
        expected_output = {1: ['a']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case_duplicates(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'b'), (5, 'e')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['c'], 4: ['b'], 5: ['e']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case_sorted_list(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['c'], 4: ['d'], 5: ['e']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_edge_case_unsorted_list(self):
        test_list = [(5, 'e'), (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
        expected_output = {1: ['a'], 2: ['b'], 3: ['c'], 4: ['d'], 5: ['e']}
        self.assertEqual(group_element(test_list), expected_output)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            group_element('invalid input')

    def test_invalid_input_non_tuple(self):
        test_list = ['invalid input']
        with self.assertRaises(TypeError):
            group_element(test_list)

    def test_invalid_input_non_integer(self):
        test_list = [(1, 'a'), ('invalid input', 'b')]
        with self.assertRaises(TypeError):
            group_element(test_list)
