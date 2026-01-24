import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_simple_input(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        expected_output = {'a': [1], 'b': [2], 'c': [3]}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_edge_conditions(self):
        # Test with empty list
        test_list = []
        expected_output = {}
        self.assertEqual(assign_elements(test_list), expected_output)

        # Test with list containing only one element
        test_list = [(1, 'a')]
        expected_output = {'a': [1]}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_complex_scenarios(self):
        # Test with duplicate values
        test_list = [(1, 'a'), (2, 'a'), (3, 'b')]
        expected_output = {'a': [1, 2], 'b': [3]}
        self.assertEqual(assign_elements(test_list), expected_output)

        # Test with duplicate keys
        test_list = [(1, 'a'), (1, 'b')]
        expected_output = {'a': [1], 'b': [1]}
        self.assertEqual(assign_elements(test_list), expected_output)
