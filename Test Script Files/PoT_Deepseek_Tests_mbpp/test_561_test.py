import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        expected = {'a': [1], 'b': [2], 'c': [3]}
        self.assertEqual(assign_elements(test_list), expected)

    def test_empty_list(self):
        test_list = []
        expected = {}
        self.assertEqual(assign_elements(test_list), expected)

    def test_duplicate_values(self):
        test_list = [(1, 'a'), (2, 'a'), (3, 'b')]
        expected = {'a': [1, 2], 'b': [3]}
        self.assertEqual(assign_elements(test_list), expected)

    def test_duplicate_keys(self):
        test_list = [(1, 'a'), (1, 'b')]
        expected = {'a': [1], 'b': [1]}
        self.assertEqual(assign_elements(test_list), expected)

    def test_single_element(self):
        test_list = [(1, 'a')]
        expected = {'a': [1]}
        self.assertEqual(assign_elements(test_list), expected)
