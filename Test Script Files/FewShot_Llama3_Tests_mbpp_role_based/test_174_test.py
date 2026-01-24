import unittest
from mbpp_174_code import group_keyvalue

class TestGroupKeyvalue(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(group_keyvalue([]), {})

    def test_single_keyvalue_pair(self):
        self.assertEqual(group_keyvalue([("a", 1)]), {"a": [1]})

    def test_multiple_keyvalue_pairs(self):
        self.assertEqual(group_keyvalue([("a", 1), ("a", 2), ("b", 3)]), {"a": [1, 2], "b": [3]})

    def test_keyvalue_pairs_with_duplicates(self):
        self.assertEqual(group_keyvalue([("a", 1), ("a", 1), ("b", 3)]), {"a": [1, 1], "b": [3]})

    def test_keyvalue_pairs_with_empty_values(self):
        self.assertEqual(group_keyvalue([("a", ""), ("b", 3)]), {"a": [""], "b": [3]})

    def test_keyvalue_pairs_with_non_hashable_keys(self):
        with self.assertRaises(TypeError):
            group_keyvalue([(None, 1)])
