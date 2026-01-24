import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(merge_dict({}, {}), {})

    def test_single_input(self):
        self.assertEqual(merge_dict({'a': 1}, {}), {'a': 1})

    def test_merge(self):
        self.assertEqual(merge_dict({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_update_overrides(self):
        self.assertEqual(merge_dict({'a': 1, 'b': 2}, {'a': 3, 'c': 4}), {'a': 3, 'b': 2, 'c': 4})

    def test_update_ignores(self):
        self.assertEqual(merge_dict({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_update_overrides_with_empty(self):
        self.assertEqual(merge_dict({'a': 1, 'b': 2}, {}), {'a': 1, 'b': 2})

    def test_update_ignores_with_empty(self):
        self.assertEqual(merge_dict({}, {'c': 3, 'd': 4}), {'c': 3, 'd': 4})
