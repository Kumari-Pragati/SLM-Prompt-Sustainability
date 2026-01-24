import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_empty_dict(self):
        self.assertDictEqual({}, drop_empty({}))

    def test_dict_with_empty_values(self):
        self.assertDictEqual({'key1': None, 'key2': ''}, drop_empty({'key1': None, 'key2': ''}))

    def test_dict_with_mixed_values(self):
        self.assertDictEqual({'key1': 1, 'key2': 'str', 'key3': None, 'key4': []}, drop_empty({'key1': 1, 'key2': 'str', 'key3': None, 'key4': []}))

    def test_dict_with_only_empty_values(self):
        self.assertDictEqual({}, drop_empty({None, '', [], (), set()}))

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            drop_empty([1, 2, None])

    def test_invalid_input_type_set(self):
        with self.assertRaises(TypeError):
            drop_empty({1, 2, None})
