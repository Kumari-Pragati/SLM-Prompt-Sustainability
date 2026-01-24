import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(dict_filter({}, 0), {})

    def test_no_matching_values(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(dict_filter(dict1, 5), {})

    def test_matching_values(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(dict_filter(dict1, 3), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_negative_values(self):
        dict1 = {'a': -1, 'b': -2, 'c': -3}
        self.assertEqual(dict_filter(dict1, 0), {'a': -1, 'b': -2, 'c': -3})

    def test_non_integer_values(self):
        dict1 = {'a': 'hello', 'b': 2, 'c': 3.5}
        self.assertEqual(dict_filter(dict1, 3), {'b': 2})
