import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(get_key({"a": 1, "b": 2, "c": 3}), ["a", "b", "c"])

    def test_empty_dict(self):
        self.assertListEqual(get_key({}), [])

    def test_single_key_dict(self):
        self.assertListEqual(get_key({"key": "value"}), ["key"])

    def test_keys_with_numbers(self):
        self.assertListEqual(get_key({0: "zero", 1: "one", 2: "two"}), [0, 1, 2])

    def test_keys_with_mixed_types(self):
        self.assertListEqual(get_key({1.23: "one", "two": 2, True: False}), [1.23, "two", True])

    def test_keys_with_special_characters(self):
        self.assertListEqual(get_key({"!@#$%^&*()": "value"}), ["!@#$%^&*()"])

    def test_keys_with_whitespace(self):
        self.assertListEqual(get_key({"key1": "value", "key 2": "value"}), ["key1", "key 2"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_key(123)
