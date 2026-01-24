import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):
    def test_merge_empty_dictionaries(self):
        self.assertDictEqual(merge_dictionaries({}, {}), {})

    def test_merge_single_dictionary(self):
        self.assertDictEqual(merge_dictionaries({"a": 1}, {}), {"a": 1})
        self.assertDictEqual(merge_dictionaries({}, {"a": 1}), {"a": 1})

    def test_merge_identical_keys(self):
        self.assertDictEqual(merge_dictionaries({"a": 1, "b": 2}, {"a": 3, "b": 4}), {"a": 3, "b": 4})

    def test_merge_different_types(self):
        self.assertRaises(TypeError, merge_dictionaries, {"a": 1}, {"a": [1, 2, 3]})

    def test_merge_nested_dictionaries(self):
        dict1 = {"a": {"x": 1, "y": 2}, "b": 3}
        dict2 = {"a": {"z": 4}, "c": 5}
        expected_result = {"a": {"x": 1, "y": 2, "z": 4}, "b": 3, "c": 5}
        self.assertDictEqual(merge_dictionaries(dict1, dict2), expected_result)
