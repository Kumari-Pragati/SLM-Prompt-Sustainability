import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):

    def test_group_keyvalue(self):
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2), ('b', 3), ('c', 4)]), {'a': [1, 2], 'b': [3], 'c': [4]})
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3), ('c', 4)]), {'a': [1, 3], 'b': [2], 'c': [4]})
        self.assertEqual(group_keyvalue([]), {})
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2), ('a', 3)]), {'a': [1, 2, 3]})
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('c', 3), ('d', 4)]), {'a': [], 'b': [], 'c': [], 'd': []})
