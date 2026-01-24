import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(dict_filter({}, 0), {})

    def test_no_matching_values(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3}, 5), {})

    def test_single_match(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3}, 2), {'b': 2})

    def test_multiple_matches(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 2), {'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_max_value(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 5), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_min_value(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 1), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_dict_with_negative_values(self):
        self.assertEqual(dict_filter({'a': -1, 'b': 2, 'c': 3, 'd': -4, 'e': 5}, 0), {'b': 2, 'c': 3, 'e': 5})
