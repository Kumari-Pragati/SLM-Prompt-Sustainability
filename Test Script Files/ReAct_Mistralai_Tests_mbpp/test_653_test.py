import unittest
from mbpp_653_code import grouping_Dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_empty_list(self):
        result = grouping_Dictionary([])
        self.assertDictEqual(result, {})

    def test_single_item(self):
        result = grouping_Dictionary([('key', 'value')])
        self.assertDictEqual(result, {'key': ['value']})

    def test_multiple_items(self):
        result = grouping_Dictionary([('key1', 'value1'), ('key2', 'value2'), ('key1', 'value3')])
        self.assertDictEqual(result, {'key1': ['value1', 'value3'], 'key2': ['value2']})

    def test_duplicate_keys(self):
        result = grouping_Dictionary([('key', 'value1'), ('key', 'value2'), ('another_key', 'value3')])
        self.assertDictEqual(result, {'key': ['value1', 'value2'], 'another_key': ['value3']})

    def test_keys_with_spaces(self):
        result = grouping_Dictionary([('key with spaces', 'value')])
        self.assertDictEqual(result, {'key with spaces': ['value']})

    def test_keys_with_special_characters(self):
        result = grouping_Dictionary([('key#1', 'value')])
        self.assertDictEqual(result, {'key#1': ['value']})

    def test_keys_with_empty_string(self):
        with self.assertRaises(ValueError):
            grouping_Dictionary([( '', 'value' )])

    def test_values_with_none(self):
        result = grouping_Dictionary([('key', None)])
        self.assertDictEqual(result, {'key': []})
