import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(get_key({}), [])

    def test_single_key_dict(self):
        self.assertEqual(get_key({'key': 'value'}), ['key'])

    def test_multiple_keys_dict(self):
        self.assertEqual(get_key({'key1': 'value1', 'key2': 'value2'}), ['key1', 'key2'])

    def test_key_with_spaces(self):
        self.assertEqual(get_key({'key with spaces': 'value'}), ['key with spaces'])

    def test_key_with_special_characters(self):
        self.assertEqual(get_key({'key@#$%^&*()': 'value'}), ['key@#$%^&*()'])

    def test_key_with_numbers(self):
        self.assertEqual(get_key({'key1': 'value', '1key': 'value'}), ['key1', '1key'])
