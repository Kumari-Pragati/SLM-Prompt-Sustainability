import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (1, 1), (3, 3), (2, 2)]), {'1': [(1, 1), (1, 1)], '2': [(2, 2), (2, 2)], '3': [(3, 3)]})

    def test_empty_list(self):
        self.assertDictEqual(group_element([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(group_element([(1, 1)]), {'1': [(1, 1)]})

    def test_list_with_duplicate_keys(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (1, 1), (3, 3), (2, 2), (1, 1)]), {'1': [(1, 1), (1, 1), (1, 1)], '2': [(2, 2), (2, 2)], '3': [(3, 3)]})

    def test_list_with_duplicate_values(self):
        self.assertDictEqual(group_element([(1, 1), (1, 1), (2, 2), (2, 2)]), {'1': [(1, 1), (1, 1)], '2': [(2, 2), (2, 2)]})

    def test_list_with_unsorted_elements(self):
        self.assertDictEqual(group_element([(3, 3), (1, 1), (2, 2), (1, 1)]), {'1': [(1, 1), (1, 1)], '2': [(2, 2)], '3': [(3, 3)]})

    def test_list_with_non_tuple_elements(self):
        with self.assertRaises(TypeError):
            group_element([1, 2, 3])
