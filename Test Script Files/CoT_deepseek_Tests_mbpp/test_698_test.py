import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_empty_dict(self):
        test_dict = {}
        expected_output = {}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_single_item_dict(self):
        test_dict = {'a': 1}
        expected_output = {'a': 1}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_negative_values(self):
        test_dict = {'b': -2, 'a': -1, 'd': -4, 'c': -3}
        expected_output = {'a': -1, 'b': -2, 'c': -3, 'd': -4}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_duplicate_values(self):
        test_dict = {'b': 2, 'a': 1, 'd': 2, 'c': 1}
        expected_output = {'a': 1, 'c': 1, 'b': 2, 'd': 2}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_key_with_tuple_value(self):
        test_dict = {(1, 2): 2, (1, 1): 1, (2, 2): 2, (2, 1): 1}
        expected_output = {(1, 1): 1, (1, 2): 2, (2, 1): 1, (2, 2): 2}
        self.assertEqual(sort_dict_item(test_dict), expected_output)
