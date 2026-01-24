import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyValue(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2)]), {'a': [1], 'b': [2]})

    def test_edge_conditions(self):
        self.assertEqual(group_keyvalue([]), {})
        self.assertEqual(group_keyvalue([('a', 1), ('a', 2)]), {'a': [1, 2]})

    def test_complex_cases(self):
        self.assertEqual(group_keyvalue([('a', 1), ('b', 2), ('a', 3)]), {'a': [1, 3], 'b': [2]})
