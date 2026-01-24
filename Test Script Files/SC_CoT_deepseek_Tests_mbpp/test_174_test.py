import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3)]), {'a': [1, 3], 'b': [2]})

    def test_empty_list(self):
        self.assertEqual(group_keyvalue([]), {})

    def test_single_element(self):
        self.assertEqual(group_keyvalue([('a', 1)]), {'a': [1]})

    def test_duplicate_keys(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2)]), {'a': [1, 2]})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            group_keyvalue('not a list')

        with self.assertRaises(TypeError):
            group_keyvalue([('a', 1), 1])

        with self.assertRaises(TypeError):
            group_keyvalue([1, ('a', 1)])

        with self.assertRaises(TypeError):
            group_keyvalue([('a', 'not a number')])
