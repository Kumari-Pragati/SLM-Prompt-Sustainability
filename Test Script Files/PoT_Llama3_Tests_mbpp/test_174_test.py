import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3)]), {'a': [1, 3], 'b': [2]})

    def test_edge_case_empty_input(self):
        self.assertEqual(group_keyvalue([]), {})

    def test_edge_case_single_key(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2)]), {'a': [1, 2]})

    def test_edge_case_single_value(self):
        self.assertEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_edge_case_multiple_keys(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('c', 3)]), {'a': [1], 'b': [2], 'c': [3]})

    def test_edge_case_key_value_pair(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3), ('b', 4)]), {'a': [1, 3], 'b': [2, 4]})

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            group_keyvalue([1, 2, 3])
