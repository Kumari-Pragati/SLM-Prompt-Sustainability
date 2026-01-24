import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_sort_dict_item(self):
        test_dict = {'a': 1, 'c': 3, 'b': 2}
        self.assertEqual(sort_dict_item(test_dict), {'b': 2, 'a': 1, 'c': 3})

    def test_sort_dict_item_empty_dict(self):
        test_dict = {}
        self.assertEqual(sort_dict_item(test_dict), {})

    def test_sort_dict_item_single_key(self):
        test_dict = {'a': 1}
        self.assertEqual(sort_dict_item(test_dict), {'a': 1})

    def test_sort_dict_item_multiple_keys(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(sort_dict_item(test_dict), {'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1})
