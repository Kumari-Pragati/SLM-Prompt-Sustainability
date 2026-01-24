import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(group_keyvalue([('a', 1), ('a', 2), ('b', 3)]), {'a': [1, 2], 'b': [3]})
        self.assertDictEqual(group_keyvalue([('a', 1), ('a', 2), ('a', 3)]), {'a': [1, 2, 3]})

    def test_edge_cases(self):
        self.assertDictEqual(group_keyvalue([('a', 1)]), {'a': [1]})
        self.assertDictEqual(group_keyvalue([('a', 1), ('a', 1)]), {'a': [1, 1]})
        self.assertDictEqual(group_keyvalue([('a', 1), ('b', 1)]), {'a': [1], 'b': [1]})

    def test_complex(self):
        self.assertDictEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3), ('b', 4), ('a', 1)]), {'a': [1, 3, 1], 'b': [2, 4]})
