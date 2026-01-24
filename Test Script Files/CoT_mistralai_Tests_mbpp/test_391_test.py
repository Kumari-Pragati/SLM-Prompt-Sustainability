import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(convert_list_dictionary([], [], []), [])
        self.assertListEqual(convert_list_dictionary([], ['a'], []), [])
        self.assertListEqual(convert_list_dictionary([], [], ['a']) , [])
        self.assertListEqual(convert_list_dictionary([], ['a'], ['b']) , [])

    def test_single_element_lists(self):
        self.assertListEqual(convert_list_dictionary(['a'], ['b'], ['c']), [{'a': {'b': 'c'}}])
        self.assertListEqual(convert_list_dictionary(['a'], ['b'], [1]) , [{'a': {'b': 1}})
        self.assertListEqual(convert_list_dictionary([1], ['a'], ['b']) , [{1: {'a': 'b'}})

    def test_multiple_elements_lists(self):
        self.assertListEqual(convert_list_dictionary(['a', 'b'], ['x', 'y'], ['1', '2']) , [{'a': {'x': '1'}, 'b': {'y': '2'}})
        self.assertListEqual(convert_list_dictionary(['a', 'b'], ['x', 'y'], [1, 2]) , [{'a': {'x': 1}, 'b': {'y': 2}})
        self.assertListEqual(convert_list_dictionary([1, 2], ['a', 'b'], ['x', 'y']) , [{'1': {'a': 'x'}, '2': {'b': 'y'}})

    def test_mixed_types(self):
        self.assertRaises(TypeError, convert_list_dictionary, [1, 'a'], ['b'], [1])
        self.assertRaises(TypeError, convert_list_dictionary, [1, 'a'], ['b'], ['a'])
        self.assertListEqual(convert_list_dictionary([1, 'a'], ['b'], [1, 'a']) , [{'1': {'b': 1}, 'a': {'b': 'a'}})
