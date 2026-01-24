import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(group_keyvalue([]), {})

    def test_single_keyvalue(self):
        self.assertEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_multiple_keyvalues(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2), ('b', 3)]), {'a': [1, 2], 'b': [3]})

    def test_keyvalue_with_duplicates(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 1), ('b', 3)]), {'a': [1, 1], 'b': [3]})

    def test_keyvalue_with_empty_list(self):
        self.assertEqual(group_keyvalue([('a', []), ('b', 3)]), {'a': [], 'b': [3]})

    def test_keyvalue_with_non_list_value(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 3)]), {'a': [1], 'b': [3]})
