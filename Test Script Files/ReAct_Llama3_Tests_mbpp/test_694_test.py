import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(extract_unique({}), [])

    def test_single_value_dict(self):
        self.assertEqual(extract_unique({'a': [1]}), [1])

    def test_multiple_values_dict(self):
        self.assertEqual(extract_unique({'a': [1, 2], 'b': [2, 3]}), [1, 2, 3])

    def test_dict_with_duplicates(self):
        self.assertEqual(extract_unique({'a': [1, 1, 2, 2]}), [1, 2])

    def test_dict_with_empty_list(self):
        self.assertEqual(extract_unique({'a': [], 'b': [1, 2]}), [])

    def test_dict_with_single_empty_list(self):
        self.assertEqual(extract_unique({'a': [1], 'b': []}), [1])

    def test_dict_with_empty_dict(self):
        self.assertEqual(extract_unique({'a': {}, 'b': [1, 2]}), [1, 2])

    def test_dict_with_single_empty_dict(self):
        self.assertEqual(extract_unique({'a': [1], 'b': {}}), [1])
