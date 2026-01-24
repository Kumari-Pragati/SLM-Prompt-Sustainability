import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_assign_elements_typical(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        expected_output = {1: ['a'], 2: ['b'], 3: ['a', 'b', 'c']}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_assign_elements_edge_case_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_assign_elements_edge_case_single_element(self):
        test_list = [('a', 1)]
        expected_output = {1: ['a']}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_assign_elements_edge_case_duplicate_values(self):
        test_list = [('a', 1), ('b', 1)]
        expected_output = {1: ['a', 'b']}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_assign_elements_invalid_input_non_list(self):
        test_list = 'not a list'
        with self.assertRaises(TypeError):
            assign_elements(test_list)

    def test_assign_elements_invalid_input_non_tuple(self):
        test_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            assign_elements(test_list)
