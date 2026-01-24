import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):
    def test_typical_use_case(self):
        test_dict = {'a': 1, 'c': 3, 'b': 2}
        expected_result = {'b': 2, 'a': 1, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_empty_dict(self):
        test_dict = {}
        expected_result = {}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_dict_with_single_item(self):
        test_dict = {'a': 1}
        expected_result = {'a': 1}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_dict_with_multiple_items(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        expected_result = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_dict_with_negative_values(self):
        test_dict = {'a': -1, 'b': -2, 'c': -3, 'd': -4}
        expected_result = {'d': -4, 'c': -3, 'b': -2, 'a': -1}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_dict_with_non_integer_values(self):
        test_dict = {'a': 1.5, 'b': 2.5, 'c': 3.5, 'd': 4.5}
        expected_result = {'d': 4.5, 'c': 3.5, 'b': 2.5, 'a': 1.5}
        self.assertEqual(sort_dict_item(test_dict), expected_result)
