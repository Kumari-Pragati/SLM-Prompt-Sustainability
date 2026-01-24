import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_empty_dictionary(self):
        self.assertFalse(is_key_present({}, 'key'))

    def test_non_existent_key(self):
        self.assertFalse(is_key_present({'key1': 'value1', 'key3': 'value3'}, 'key2'))

    def test_existent_key(self):
        self.assertTrue(is_key_present({'key': 'value'}, 'key'))

    def test_key_with_value_none(self):
        self.assertTrue(is_key_present({'key': None}, 'key'))

    def test_key_with_empty_string_value(self):
        self.assertTrue(is_key_present({'key': ''}, 'key'))
