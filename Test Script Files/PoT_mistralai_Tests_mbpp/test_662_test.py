import unittest
from mbpp_662_code import MutableMapping

class TestSortedDict(unittest.TestCase):

    def test_typical_case(self):
        data = {
            'apples': ['red', 'green', 'yellow'],
            'oranges': ['orange', 'yellow', 'green'],
            'bananas': ['yellow', 'green', 'red']
        }
        expected = {
            'apples': ['green', 'red', 'yellow'],
            'oranges': ['green', 'orange', 'yellow'],
            'bananas': ['green', 'red', 'yellow']
        }
        self.assertDictEqual(sorted_dict(data), expected)

    def test_empty_dict(self):
        self.assertDictEqual(sorted_dict({}), {})

    def test_single_key(self):
        self.assertDictEqual(sorted_dict({'apples': ['red']}), {'apples': ['red']})

    def test_single_value(self):
        self.assertDictEqual(sorted_dict({'apples': ['red', 'red']}), {'apples': ['red', 'red']})

    def test_mixed_types(self):
        data = {
            1: 2,
            'apples': ['red', 'green', 'yellow'],
            (1, 2): [3, 4]
        }
        expected = {
            1: 2,
            'apples': ['green', 'red', 'yellow'],
            (1, 2): [3, 4]
        }
        self.assertDictEqual(sorted_dict(data), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sorted_dict(123)
