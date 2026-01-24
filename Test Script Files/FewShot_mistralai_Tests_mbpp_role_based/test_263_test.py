import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):
    def test_merge_empty_dicts(self):
        self.assertEqual(merge_dict({}, {}), {})

    def test_merge_single_dict(self):
        self.assertEqual(merge_dict({"a": 1}, {}), {"a": 1})
        self.assertEqual(merge_dict({}, {"a": 1}), {"a": 1})

    def test_merge_two_dicts(self):
        self.assertEqual(merge_dict({"a": 1, "b": 2}, {"b": 3, "c": 4}), {"a": 1, "b": 3, "c": 4})

    def test_merge_overwrite_keys(self):
        self.assertEqual(merge_dict({"a": 1, "b": 2}, {"a": 3, "c": 4}), {"a": 3, "b": 2, "c": 4})

    def test_merge_different_types(self):
        self.assertRaises(TypeError, merge_dict, {"a": 1}, [2, 3])
