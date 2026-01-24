import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_dict_filter_positive(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(dict_filter(test_dict, 2), {'b': 2, 'c': 3, 'd': 4})

    def test_dict_filter_negative(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(dict_filter(test_dict, 3), {'d': 4})

    def test_dict_filter_zero(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(dict_filter(test_dict, 0), test_dict)

    def test_dict_filter_empty(self):
        test_dict = {}
        self.assertEqual(dict_filter(test_dict, 2), {})

    def test_dict_filter_none(self):
        self.assertIsNone(dict_filter(None, 2))
