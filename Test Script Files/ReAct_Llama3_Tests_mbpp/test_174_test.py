import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(group_keyvalue([]), {})

    def test_single_keyvalue(self):
        self.assertEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_multiple_keyvalues(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2), ('b', 3)]), {'a': [1, 2], 'b': [3]})

    def test_keyvalue_duplicates(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 1), ('b', 3)]), {'a': [1, 1], 'b': [3]})

    def test_keyvalue_order(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3)]), {'a': [1, 3], 'b': [2]})

    def test_keyvalue_empty_value(self):
        self.assertEqual(group_keyvalue([('a', None), ('b', 2)]), {'a': [None], 'b': [2]})

    def test_keyvalue_non_hashable_key(self):
        with self.assertRaises(TypeError):
            group_keyvalue([(None, 1)])
