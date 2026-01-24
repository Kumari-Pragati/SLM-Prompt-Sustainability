import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(group_element([]), {})

    def test_single_element(self):
        self.assertDictEqual(group_element([(1, 1)]), {'1': [(1, 1)]})

    def test_multiple_elements_same_key(self):
        self.assertDictEqual(group_element([(1, 1), (1, 1), (2, 2), (2, 2)]), {'1': [(1, 1), (1, 1)], '2': [(2, 2), (2, 2)]})

    def test_multiple_elements_different_keys(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (3, 3)]), {'1': [(1, 1)], '2': [(2, 2)], '3': [(3, 3)]})

    def test_mixed_keys_sorted(self):
        self.assertDictEqual(group_element([(3, 3), (2, 2), (1, 1)]), {'1': [(1, 1)], '2': [(2, 2)], '3': [(3, 3)]})

    def test_mixed_keys_unsorted(self):
        self.assertDictEqual(group_element([(2, 2), (3, 3), (1, 1)]), {'1': [(1, 1)], '2': [(2, 2)], '3': [(3, 3)]})

    def test_duplicate_values(self):
        self.assertDictEqual(group_element([(1, 1), (1, 1), (2, 2), (2, 2), (1, 1)]), {'1': [(1, 1), (1, 1), (1, 1)], '2': [(2, 2), (2, 2)]})

    def test_negative_key(self):
        with self.assertRaises(KeyError):
            group_element([(-1, 1)]))

    def test_non_hashable_key(self):
        with self.assertRaises(TypeError):
            group_element([(1, 'str')])
