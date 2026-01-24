import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(sort_dict_item({}), {})

    def test_single_item_dict(self):
        self.assertEqual(sort_dict_item({'a': 1}), {'a': 1})

    def test_multiple_items_dict(self):
        self.assertEqual(sort_dict_item({'a': 1, 'b': 2, 'c': 3}), {'c': 3, 'b': 2, 'a': 1})

    def test_dict_with_negative_values(self):
        self.assertEqual(sort_dict_item({'a': -1, 'b': 2, 'c': 3}), {'c': 3, 'b': 2, 'a': -1})

    def test_dict_with_zero_values(self):
        self.assertEqual(sort_dict_item({'a': 0, 'b': 2, 'c': 3}), {'c': 3, 'b': 2, 'a': 0})

    def test_dict_with_duplicates(self):
        self.assertEqual(sort_dict_item({'a': 1, 'b': 2, 'c': 1}), {'c': 1, 'b': 2, 'a': 1})

    def test_dict_with_empty_values(self):
        self.assertEqual(sort_dict_item({'a': '', 'b': 2, 'c': 3}), {'c': 3, 'b': 2, 'a': ''})
