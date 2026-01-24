import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_key_present(self):
        dictionary = {"a": 1, "b": 2, "c": 3}
        self.assertTrue(is_key_present(dictionary, "b"))

    def test_key_absent(self):
        dictionary = {"a": 1, "b": 2, "c": 3}
        self.assertFalse(is_key_present(dictionary, "d"))

    def test_key_present_with_empty_dict(self):
        dictionary = {}
        self.assertFalse(is_key_present(dictionary, "a"))

    def test_key_absent_with_empty_dict(self):
        dictionary = {}
        self.assertFalse(is_key_present(dictionary, "a"))

    def test_key_present_with_single_key_dict(self):
        dictionary = {"a": 1}
        self.assertTrue(is_key_present(dictionary, "a"))

    def test_key_absent_with_single_key_dict(self):
        dictionary = {"a": 1}
        self.assertFalse(is_key_present(dictionary, "b"))
