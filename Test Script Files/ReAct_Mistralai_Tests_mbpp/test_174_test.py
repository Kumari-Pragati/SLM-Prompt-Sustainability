import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(group_keyvalue([]), {})

    def test_single_key_value(self):
        self.assertDictEqual(group_keyvalue([('key', 'value')]), {'key': ['value']})

    def test_multiple_key_values(self):
        self.assertDictEqual(group_keyvalue([('key1', 'value1'), ('key2', 'value2'), ('key1', 'value3')]),
                             {'key1': ['value1', 'value3'], 'key2': ['value2']})

    def test_duplicate_key(self):
        self.assertDictEqual(group_keyvalue([('key', 'value1'), ('key', 'value2'), ('another_key', 'value3')]),
                             {'key': ['value1', 'value2'], 'another_key': ['value3']})

    def test_key_with_space(self):
        self.assertDictEqual(group_keyvalue([('key with space', 'value')]), {'key with space': ['value']})

    def test_key_with_special_characters(self):
        self.assertDictEqual(group_keyvalue([('key#with%special$characters', 'value')]),
                             {'key#with%special$characters': ['value']})

    def test_empty_value(self):
        self.assertDictEqual(group_keyvalue([('key', '')]), {'key': []})

    def test_none_value(self):
        self.assertDictEqual(group_keyvalue([('key', None)]), {'key': []})
