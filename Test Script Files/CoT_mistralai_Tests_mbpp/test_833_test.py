import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_empty_dict(self):
        self.assertListEqual(get_key({}), [])

    def test_single_key_dict(self):
        self.assertListEqual(get_key({'key': 'value'}), ['key'])

    def test_multiple_keys_dict(self):
        self.assertListEqual(get_key({'key1': 'value1', 'key2': 'value2'}), ['key1', 'key2'])

    def test_key_with_special_characters(self):
        self.assertListEqual(get_key({'key_with_underscore': 'value'}), ['key_with_underscore'])

    def test_key_with_numbers(self):
        self.assertListEqual(get_key({'key1': 'value', '1key': 'value'}), ['key1', '1key'])

    def test_key_with_spaces(self):
        self.assertListEqual(get_key({'key with spaces': 'value'}), ['key with spaces'])

    def test_key_with_mixed_characters(self):
        self.assertListEqual(get_key({'key123_with_underscore': 'value'}), ['key123_with_underscore'])

    def test_key_with_duplicates(self):
        self.assertListEqual(get_key({'key1': 'value', 'key1': 'value'}), ['key1'])

    def test_key_with_none_value(self):
        self.assertListEqual(get_key({'key': None}), ['key'])

    def test_key_with_empty_string_value(self):
        self.assertListEqual(get_key({'key': ''}), ['key'])

    def test_key_with_list_value(self):
        self.assertListEqual(get_key({'key': [1, 2, 3]}), ['key'])

    def test_key_with_tuple_value(self):
        self.assertListEqual(get_key({'key': (1, 2, 3)}), ['key'])

    def test_key_with_set_value(self):
        self.assertListEqual(get_key({'key': set([1, 2, 3])}), ['key'])
