import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_empty_dict(self):
        self.assertDictEqual({}, drop_empty({}))

    def test_dict_with_empty_values(self):
        self.assertDictEqual({'key1': None, 'key2': '', 'key3': []}, drop_empty({'key1': None, 'key2': '', 'key3': []}))

    def test_dict_with_non_empty_values(self):
        self.assertDictEqual({'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]}, drop_empty({'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]}))
