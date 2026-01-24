import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):
    def test_sorted_dict_empty_dict(self):
        self.assertDictEqual(sorted_dict({}), {})

    def test_sorted_dict_single_key_single_value(self):
        self.assertDictEqual(sorted_dict({'a': [1, 2, 3]}), {'a': [1, 2, 3]})

    def test_sorted_dict_multiple_keys_single_value(self):
        self.assertDictEqual(sorted_dict({'a': [1, 2, 3], 'b': [4, 5, 6]}), {'a': [1, 2, 3], 'b': [4, 5, 6]})

    def test_sorted_dict_single_key_multiple_value(self):
        self.assertDictEqual(sorted_dict({'a': [3, 2, 1]}), {'a': [1, 2, 3]})

    def test_sorted_dict_multiple_keys_multiple_value(self):
        self.assertDictEqual(sorted_dict({'a': [3, 2, 1], 'b': [6, 5, 4]}), {'a': [1, 2, 3], 'b': [4, 5, 6]})

    def test_sorted_dict_mixed_types(self):
        self.assertDictEqual(sorted_dict({1: 'a', 2: 'b', 3: 'c'}), {1: ['a'], 2: ['b'], 3: ['c']})

    def test_sorted_dict_invalid_input(self):
        with self.assertRaises(TypeError):
            sorted_dict(123)
