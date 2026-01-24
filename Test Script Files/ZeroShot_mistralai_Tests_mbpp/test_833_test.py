import unittest
from mbpp_833_code import get_key  # replace 'your_module_name' with the actual name of the module containing the get_key function

class TestGetKeyFunction(unittest.TestCase):

    def test_empty_dictionary(self):
        result = get_key({})
        self.assertIsInstance(result, list)
        self.assertListEqual(result, [])

    def test_single_key_dictionary(self):
        result = get_key({"key1": "value1"})
        self.assertIsInstance(result, list)
        self.assertListEqual(result, ["key1"])

    def test_multiple_key_dictionary(self):
        result = get_key({"key1": "value1", "key2": "value2", "key3": "value3"})
        self.assertIsInstance(result, list)
        self.assertListEqual(result, ["key1", "key2", "key3"])

    def test_key_with_special_characters(self):
        result = get_key({"key1!@#": "value1"})
        self.assertIsInstance(result, list)
        self.assertListEqual(result, ["key1!@#"])
