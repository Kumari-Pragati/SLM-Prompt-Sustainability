import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_empty_dict(self):
        result = drop_empty({})
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, {})

    def test_dict_with_empty_values(self):
        result = drop_empty({'key1': None, 'key2': '', 'key3': []})
        self.assertDictEqual(result, {'key2': ''})

    def test_dict_with_mixed_types(self):
        result = drop_empty({'key1': 1, 'key2': None, 'key3': 'str', 'key4': [], 'key5': 0.0})
        self.assertDictEqual(result, {'key1': 1, 'key3': 'str', 'key5': 0.0})

    def test_dict_with_non_empty_values(self):
        result = drop_empty({'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]})
        self.assertDictEqual(result, {'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]})
