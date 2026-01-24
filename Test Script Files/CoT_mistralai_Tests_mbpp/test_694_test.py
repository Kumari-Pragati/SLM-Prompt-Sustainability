import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_unique({}), [])

    def test_single_element_list(self):
        self.assertListEqual(extract_unique({'a': ['a']}), ['a'])

    def test_multiple_elements_same(self):
        self.assertListEqual(extract_unique({'a': ['a', 'a', 'b'], 'b': ['b', 'a']}), ['a', 'b'])

    def test_multiple_elements_different(self):
        self.assertListEqual(extract_unique({'a': ['a', 'b'], 'b': ['b', 'c']}), ['a', 'b', 'c'])

    def test_duplicate_dict_key(self):
        self.assertListEqual(extract_unique({'a': ['a', 'a'], 'b': ['b', 'b']}), ['a', 'b'])

    def test_empty_value(self):
        self.assertListEqual(extract_unique({'a': [], 'b': ['b']}), ['b'])

    def test_list_with_duplicates(self):
        self.assertListEqual(extract_unique({'a': ['a', 'a', 'b', 'a']}), ['a', 'b'])

    def test_list_with_non_list_value(self):
        self.assertRaises(TypeError, extract_unique, {'a': 1, 'b': [2, 3]})

    def test_list_with_non_iterable_value(self):
        self.assertRaises(TypeError, extract_unique, {'a': 1, 'b': '2'})
