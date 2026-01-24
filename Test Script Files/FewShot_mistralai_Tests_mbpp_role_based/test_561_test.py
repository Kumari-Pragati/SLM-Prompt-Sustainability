import unittest
from mbpp_561_code import assign_elements

class TestAssignElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('a', 1), ('b', 2), ('a', 3)]
        expected_output = {'a': [1, 3], 'b': [2]}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_empty_list(self):
        self.assertEqual(assign_elements([]), {})

    def test_single_element(self):
        test_list = [('a', 'a')]
        expected_output = {'a': ['a']}
        self.assertEqual(assign_elements(test_list), expected_output)

    def test_key_not_in_list(self):
        test_list = [('a', 1), ('b', 2)]
        with self.assertRaises(KeyError):
            assign_elements(test_list)

    def test_value_not_in_list(self):
        test_list = [('a', 'a'), ('b', 1)]
        with self.assertRaises(ValueError):
            assign_elements(test_list)
