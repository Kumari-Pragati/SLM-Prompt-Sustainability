import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(group_keyvalue([]), {})

    def test_single_item_list(self):
        self.assertEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_multiple_items_list(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3)]), {'a': [1, 3], 'b': [2]})

    def test_duplicate_keys(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2)]), {'a': [1, 2]})
