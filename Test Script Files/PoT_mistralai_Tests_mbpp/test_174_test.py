import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(group_keyvalue([('a', 1), ('a', 2), ('b', 3), ('a', 4)]), {'a': [1, 2, 4], 'b': [3]})

    def test_empty_list(self):
        self.assertDictEqual(group_keyvalue([]), {})

    def test_single_item(self):
        self.assertDictEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_duplicate_keys(self):
        self.assertDictEqual(group_keyvalue([('a', 1), ('a', 1), ('b', 2)]), {'a': [1, 1], 'b': [2]})

    def test_key_not_iterable(self):
        with self.assertRaises(TypeError):
            group_keyvalue([('a', 1), (1, 2)])
