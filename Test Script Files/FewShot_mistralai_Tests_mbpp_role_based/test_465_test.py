import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(drop_empty({}), {})

    def test_dict_with_empty_values(self):
        self.assertEqual(drop_empty({'key1': None, 'key2': 'value2'}), {'key2': 'value2'})

    def test_dict_with_mixed_values(self):
        self.assertEqual(drop_empty({'key1': 1, 'key2': None, 'key3': 'value3'}), {'key1': 1, 'key3': 'value3'})

    def test_dict_with_only_empty_values(self):
        self.assertEqual(drop_empty({None, None}), {})
