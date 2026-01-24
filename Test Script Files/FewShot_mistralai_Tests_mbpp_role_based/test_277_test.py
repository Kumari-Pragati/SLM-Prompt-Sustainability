import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(dict_filter({1: 2, 3: 4, 5: 6}, 3), {3: 4, 5: 6})
        self.assertEqual(dict_filter({1: 0, 3: 4, 5: -1}, 0), {3: 4})
        self.assertEqual(dict_filter({1: -2, 3: -4, 5: -6}, -3), {1: -2, 3: -4})

    def test_empty_dict(self):
        self.assertEqual(dict_filter({}, 10), {})

    def test_negative_numbers(self):
        self.assertEqual(dict_filter({1: -2, 3: -4, 5: -6}, -7), {})

    def test_non_numeric_key(self):
        with self.assertRaises(TypeError):
            dict_filter({'a': 1, 'b': 2}, 3)

    def test_non_numeric_value(self):
        with self.assertRaises(TypeError):
            dict_filter({1: 'a', 3: 'b', 5: 'c'}, 1)
