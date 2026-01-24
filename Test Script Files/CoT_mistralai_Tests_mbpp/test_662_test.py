import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):
    def test_empty_dict(self):
        self.assertDictEqual(sorted_dict({}), {})

    def test_single_key_value(self):
        self.assertDictEqual(sorted_dict({'a': [1, 2, 3, 4, 5]}), {'a': [1, 2, 3, 4, 5]})

    def test_multiple_key_value(self):
        self.assertDictEqual(sorted_dict({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}),
                              {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})

    def test_key_with_duplicate_values(self):
        self.assertDictEqual(sorted_dict({'a': [1, 1, 2, 2, 3]}), {'a': [1, 1, 2, 2, 3]})

    def test_key_with_mixed_types(self):
        self.assertRaises(TypeError, sorted_dict, {'a': [1, 2, 3], 'b': 'test'})

    def test_key_with_empty_list(self):
        self.assertDictEqual(sorted_dict({'a': [], 'b': [4, 5, 6]}), {'a': [], 'b': [4, 5, 6]})

    def test_key_with_nested_lists(self):
        self.assertDictEqual(sorted_dict({'a': [[1, 2], [3, 4]], 'b': [5, 6, 7]}),
                              {'a': [[1, 2], [3, 4]], 'b': [5, 6, 7]})
