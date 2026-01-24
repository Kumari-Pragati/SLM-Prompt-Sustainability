import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_typical_input(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a', 'c'], 2: ['b'], 3: ['a', 'c']})

    def test_edge_case_empty_list(self):
        test_list = []
        result = assign_elements(test_list)
        self.assertEqual(result, {})

    def test_edge_case_single_element(self):
        test_list = [('a', 1)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a']})

    def test_edge_case_single_key(self):
        test_list = [('a', 1), ('b', 1)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a', 'b']})

    def test_edge_case_single_value(self):
        test_list = [('a', 1), ('a', 2)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a'], 2: ['a']})

    def test_edge_case_duplicates(self):
        test_list = [('a', 1), ('a', 1), ('b', 2)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a'], 2: ['b']})

    def test_edge_case_order_matters(self):
        test_list = [('a', 1), ('b', 2), ('c', 1)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a', 'c'], 2: ['b']})
