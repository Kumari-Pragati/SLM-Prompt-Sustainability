import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_key_present(self):
        self.assertTrue(is_key_present({"key1": 1, "key2": 2}, "key1"))

    def test_key_absent(self):
        self.assertFalse(is_key_present({"key1": 1, "key2": 2}, "key3"))

    def test_empty_dictionary(self):
        self.assertFalse(is_key_present({}, "key1"))

    def test_none_dictionary(self):
        self.assertFalse(is_key_present(None, "key1"))

    def test_non_string_key(self):
        self.assertFalse(is_key_present({1: "value"}, 1))
