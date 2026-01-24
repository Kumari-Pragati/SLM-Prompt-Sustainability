import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(group_keyvalue([]), {})

    def test_single_item(self):
        self.assertDictEqual(group_keyvalue([('key', 'value')]), {'key': ['value']})

    def test_multiple_items(self):
        self.assertDictEqual(group_keyvalue([('key1', 'value1'), ('key1', 'value2'), ('key2', 'value3')]),
                             {'key1': ['value1', 'value2'], 'key2': ['value3']})

    def test_duplicate_keys(self):
        self.assertDictEqual(group_keyvalue([('key1', 'value1'), ('key1', 'value2'), ('key2', 'value3'),
                                              ('key1', 'value4')]), {'key1': ['value1', 'value2', 'value4'],
                                                                       'key2': ['value3']})
