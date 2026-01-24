import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(sorted_dict({}), {})

    def test_single_item_dict(self):
        self.assertEqual(sorted_dict({'a': [5, 3, 1]}), {'a': [1, 3, 5]})

    def test_multiple_items_dict(self):
        self.assertEqual(sorted_dict({'a': [5, 3, 1], 'b': [10, 20, 15]}), {'a': [1, 3, 5], 'b': [10, 15, 20]})

    def test_duplicate_values_dict(self):
        self.assertEqual(sorted_dict({'a': [5, 3, 1, 3]}), {'a': [1, 3, 3, 5]})

    def test_negative_values_dict(self):
        self.assertEqual(sorted_dict({'a': [-5, -3, -1]}), {'a': [-5, -3, -1]})

    def test_mixed_values_dict(self):
        self.assertEqual(sorted_dict({'a': [-5, 3, 1]}), {'a': [-5, 1, 3]})
