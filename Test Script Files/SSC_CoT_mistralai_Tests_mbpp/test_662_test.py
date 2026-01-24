import unittest
from mbpp_662_code import MutableMapping
from collections import OrderedDict

from 662_code import sorted_dict

class TestSortedDict(unittest.TestCase):

    def test_normal_case(self):
        data = {'apples': ['red', 'green', 'yellow'], 'oranges': ['orange', 'yellow']}
        result = sorted_dict(data)
        expected = {'apples': ['green', 'red', 'yellow'], 'oranges': ['orange', 'yellow']}
        self.assertDictEqual(result, expected)

    def test_empty_dict(self):
        result = sorted_dict({})
        self.assertIsInstance(result, MutableMapping)
        self.assertDictEqual(result, {})

    def test_single_key_dict(self):
        data = {'apples': ['red']}
        result = sorted_dict(data)
        expected = {'apples': ['red']}
        self.assertDictEqual(result, expected)

    def test_sorted_list(self):
        data = {'apples': [1, 2, 3], 'oranges': [3, 2, 1]}
        result = sorted_dict(data)
        expected = {'apples': [1, 2, 3], 'oranges': [1, 2, 3]}
        self.assertDictEqual(result, expected)

    def test_key_type(self):
        data = {'1': [1, 2, 3], 'str': ['a', 'b', 'c']}
        result = sorted_dict(data)
        expected = {'1': [1, 2, 3], 'str': ['a', 'b', 'c']}
        self.assertIsInstance(result, OrderedDict)
        self.assertDictEqual(result, expected)

    def test_value_type(self):
        data = {'apples': [1, 2, 3], 'oranges': (1, 2, 3)}
        result = sorted_dict(data)
        expected = {'apples': [1, 2, 3], 'oranges': (1, 2, 3)}
        self.assertIsInstance(result, OrderedDict)
        self.assertDictEqual(result, expected)
