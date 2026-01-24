import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_empty_lists(self):
        self.assertDictEqual(convert_list_dictionary([], [], []), {})
        self.assertDictEqual(convert_list_dictionary([], ['a'], []), {'a': {}})
        self.assertDictEqual(convert_list_dictionary([], [], ['a']), {'a': {}})

    def test_single_element_lists(self):
        self.assertDictEqual(convert_list_dictionary(['a'], ['b'], ['c']), {'a': {'b': 'c'}})
        self.assertDictEqual(convert_list_dictionary(['a'], [], ['b']), {'a': {'b': None}})
        self.assertDictEqual(convert_list_dictionary([], ['a'], ['b']), {'a': {'b': None}})

    def test_lists_with_duplicates(self):
        self.assertDictEqual(convert_list_dictionary(['a', 'a'], ['b', 'c'], ['d', 'e']),
                             {'a': {'b': 'd', 'c': 'e'}})

    def test_lists_with_different_lengths(self):
        with self.assertRaises(ValueError):
            convert_list_dictionary(['a', 'b'], ['c'], ['d', 'e', 'f'])

    def test_lists_with_non-hashable_elements(self):
        with self.assertRaises(TypeError):
            convert_list_dictionary([list('abc')], [1, 2, 3], [4, 5, 6])
