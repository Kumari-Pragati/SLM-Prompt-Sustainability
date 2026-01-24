import unittest
from mbpp_653_code import defaultdict
from six.moves import range

class TestGroupingDictionary(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(grouping_Dictionary([]), {})

    def test_single_key_value(self):
        self.assertDictEqual(grouping_Dictionary([('key', 'value')]), {'key': ['value']})

    def test_multiple_key_value(self):
        self.assertDictEqual(grouping_Dictionary([('key1', 'value1'), ('key2', 'value2'), ('key1', 'value3')]),
                             {'key1': ['value1', 'value3'], 'key2': ['value2']})

    def test_duplicate_key(self):
        self.assertDictEqual(grouping_Dictionary([('key', 'value1'), ('key', 'value2'), ('key', 'value3')]),
                             {'key': ['value1', 'value2', 'value3']})

    def test_key_with_space(self):
        self.assertDictEqual(grouping_Dictionary([('key with space', 'value')]), {'key with space': ['value']})

    def test_key_with_special_characters(self):
        self.assertDictEqual(grouping_Dictionary([('key#$%^&*()', 'value')]), {'key#$%^&*()': ['value']})

    def test_key_with_numbers(self):
        self.assertDictEqual(grouping_Dictionary([('key123', 'value')]), {'key123': ['value']})

    def test_key_with_only_numbers(self):
        self.assertDictEqual(grouping_Dictionary([(123, 'value')]), {123: ['value']})

    def test_key_with_empty_string(self):
        self.assertDictEqual(grouping_Dictionary([('', 'value')]), {})

    def test_key_with_none(self):
        self.assertDictEqual(grouping_Dictionary([(None, 'value')]), {})

    def test_key_with_list(self):
        self.assertDictEqual(grouping_Dictionary([(('key',), 'value')]), {'key': ['value']})

    def test_key_with_tuple(self):
        self.assertDictEqual(grouping_Dictionary([(('key', 1), 'value')]), {'key': ['value']})

    def test_key_with_set(self):
        self.assertDictEqual(grouping_Dictionary([(set(['key']), 'value')]), {'key': ['value']})

    def test_key_with_frozenset(self):
        self.assertDictEqual(grouping_Dictionary([(frozenset(['key']), 'value')]), {'key': ['value']})

    def test_key_with_dict(self):
        self.assertDictEqual(grouping_Dictionary([(dict(a=1), 'value')]), {'a': ['value']})
