import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):

    def test_empty_dict(self):
        result = sorted_dict({})
        self.assertDictEqual(result, {})

    def test_single_key_value_pair(self):
        result = sorted_dict({'a': [1, 2, 3]})
        self.assertDictEqual(result, {'a': [1, 2, 3]})

    def test_multiple_key_value_pairs(self):
        result = sorted_dict({'a': [3, 1, 2], 'b': [4, 1, 5, 9]})
        self.assertDictEqual(result, {'a': [1, 2, 3], 'b': [1, 4, 5, 9]})

    def test_key_with_empty_list(self):
        result = sorted_dict({'a': [], 'b': [4, 1, 5, 9]})
        self.assertDictEqual(result, {'a': [], 'b': [1, 4, 5, 9]})

    def test_key_with_single_item(self):
        result = sorted_dict({'a': [1], 'b': [4, 1, 5, 9]})
        self.assertDictEqual(result, {'a': [1], 'b': [1, 4, 5, 9]})

    def test_key_with_duplicate_items(self):
        result = sorted_dict({'a': [1, 1, 2, 3], 'b': [4, 1, 5, 9]})
        self.assertDictEqual(result, {'a': [1, 1, 2, 3], 'b': [1, 4, 5, 9]})

    def test_key_with_mixed_types(self):
        with self.assertRaises(TypeError):
            sorted_dict({'a': [1, 2, 3], 'b': 'apple'})

    def test_key_with_non_iterable_value(self):
        with self.assertRaises(TypeError):
            sorted_dict({'a': 1, 'b': 'apple'})
