import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a'], 2: ['b'], 3: ['a', 'c']})

    def test_empty_list(self):
        test_list = []
        result = assign_elements(test_list)
        self.assertEqual(result, {})

    def test_single_element_list(self):
        test_list = [('a', 1)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a']})

    def test_duplicate_values(self):
        test_list = [('a', 1), ('b', 1), ('c', 2)]
        result = assign_elements(test_list)
        self.assertEqual(result, {1: ['a', 'b'], 2: ['c']})

    def test_empty_key_value_pair(self):
        test_list = []
        result = assign_elements(test_list)
        self.assertEqual(result, {})
