import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):
    def test_sort_dict_with_positive_numbers(self):
        test_dict = {('a', 3): 1, ('b', 2): 2, ('c', 1): 3}
        expected_result = {('a', 3): 1, ('c', 1): 3, ('b', 2): 2}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_with_negative_numbers(self):
        test_dict = {('a', -3): 1, ('b', -2): 2, ('c', -1): 3}
        expected_result = {('a', -3): 1, ('c', -1): 3, ('b', -2): 2}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_with_zero(self):
        test_dict = {('a', 0): 1, ('b', 0): 2, ('c', 0): 3}
        expected_result = {('a', 0): 1, ('c', 0): 3, ('b', 0): 2}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_with_mixed_signs(self):
        test_dict = {('a', 3): 1, ('b', -2): 2, ('c', 1): -3}
        expected_result = {('a', 3): 1, ('c', 1): -3, ('b', -2): 2}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_with_empty_key(self):
        test_dict = {(None, 3): 1, (None, 2): 2, (None, 1): 3}
        expected_result = {(None, 3): 1, (None, 1): 3, (None, 2): 2}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_with_empty_value(self):
        test_dict = {('a', 3): None, ('b', 2): None, ('c', 1): None}
        expected_result = {('a', 3): None, ('c', 1): None, ('b', 2): None}
        self.assertEqual(sort_dict_item(test_dict), expected_result)
