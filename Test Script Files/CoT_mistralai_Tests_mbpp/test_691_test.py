import unittest
from mbpp_691_code import Iterable
from 691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(group_element([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(group_element([(1, 1)]), {'1': [(1, 1)]})

    def test_multiple_elements_same_key(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (1, 1)]), {'1': [(1, 1), (1, 1)], '2': [(2, 2)]})

    def test_multiple_elements_different_key(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (3, 3)]), {'1': [(1, 1)], '2': [(2, 2)], '3': [(3, 3)]})

    def test_mixed_data_types(self):
        self.assertRaises(TypeError, group_element, [(1, 1), (2, '2'), (3, 3.0)])

    def test_invalid_key(self):
        self.assertRaises(KeyError, group_element, [(None, 1), (1, 1)])

    def test_invalid_value(self):
        self.assertRaises(TypeError, group_element, [(1, None), (1, 1)])

    def test_duplicate_key_and_value(self):
        self.assertDictEqual(group_element([(1, 1), (1, 1)]), {'1': [(1, 1), (1, 1)]})

    def test_list_with_non_iterable_element(self):
        self.assertRaises(TypeError, group_element, [(1, [1]), (2, 2)])
