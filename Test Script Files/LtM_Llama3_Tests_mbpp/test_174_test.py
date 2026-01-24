import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(group_keyvalue([]), {})

    def test_single_keyvalue(self):
        self.assertEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_multiple_keyvalues(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2), ('b', 3)]), {'a': [1, 2], 'b': [3]})

    def test_keyvalue_duplicates(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 1), ('b', 3)]), {'a': [1, 1], 'b': [3]})

    def test_empty_key(self):
        self.assertEqual(group_keyvalue([('None', 1), ('', 2)]), {'None': [1], '': [2]})

    def test_empty_value(self):
        self.assertEqual(group_keyvalue([('a', '')]), {'a': ['',]})

    def test_keyvalue_mixed_types(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', '2'), ('c', 3.0)]), {'a': [1], 'b': ['2'], 'c': [3.0]})
