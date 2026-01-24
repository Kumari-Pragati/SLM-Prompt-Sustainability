import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):
    def test_normal_usage(self):
        self.assertDictEqual(group_keyvalue([('a', 1), ('a', 2), ('b', 3)]), {'a': [1, 2], 'b': [3]})

    def test_empty_list(self):
        self.assertDictEqual(group_keyvalue([]), {})

    def test_single_item(self):
        self.assertDictEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_key_none(self):
        with self.assertRaises(TypeError):
            group_keyvalue([(None, 1)]))

    def test_key_empty_string(self):
        with self.assertRaises(TypeError):
            group_keyvalue([('', 1)]))

    def test_key_numeric(self):
        with self.assertRaises(TypeError):
            group_keyvalue([(1, 1)]))

    def test_value_none(self):
        with self.assertRaises(TypeError):
            group_keyvalue([('a', None)]))

    def test_value_empty_list(self):
        with self.assertRaises(TypeError):
            group_keyvalue([('a', [])])
