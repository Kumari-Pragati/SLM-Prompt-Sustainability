import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(group_keyvalue([]), {})

    def test_single_item(self):
        self.assertDictEqual(group_keyvalue([('key', 'value')]), {'key': ['value']})

    def test_multiple_items(self):
        self.assertDictEqual(group_keyvalue([('key1', 'value1'), ('key2', 'value2'), ('key1', 'value3')]),
                             {'key1': ['value1', 'value3'], 'key2': ['value2']})

    def test_duplicate_keys(self):
        self.assertDictEqual(group_keyvalue([('key', 'value1'), ('key', 'value2'), ('another_key', 'value3')]),
                             {'key': ['value1', 'value2'], 'another_key': ['value3']})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            group_keyvalue([(1, 2), ('key', 3)])
