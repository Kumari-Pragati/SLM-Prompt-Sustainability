import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):
    def test_empty_dicts(self):
        self.assertEqual(merge_dict({}, {}), {})

    def test_single_dict(self):
        self.assertEqual(merge_dict({'a': 1}, {}), {'a': 1})
        self.assertEqual(merge_dict({}, {'a': 1}), {'a': 1})

    def test_overlapping_keys(self):
        self.assertEqual(merge_dict({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})

    def test_nested_dicts(self):
        d1 = {'a': {'x': 1, 'y': 2}, 'b': 3}
        d2 = {'a': {'z': 3, 'y': 4}, 'c': 5}
        expected = {'a': {'x': 1, 'y': 4, 'z': 3}, 'b': 3, 'c': 5}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            merge_dict(1, {})

    def test_invalid_input_2(self:
        with self.assertRaises(TypeError):
            merge_dict({}, 1)
