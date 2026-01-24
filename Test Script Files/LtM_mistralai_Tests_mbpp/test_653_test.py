import unittest
from mbpp_653_code import defaultdict
from six.moves import range

from653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_simple_input(self):
        data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {'a': [1, 2], 'b': [3, 4]})

    def test_empty_input(self):
        result = grouping_dictionary([])
        self.assertDictEqual(result, {})

    def test_single_key_input(self):
        data = [('a', 1), ('a', 2)]
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {'a': [1, 2]})

    def test_duplicate_key_input(self):
        data = [('a', 1), ('a', 2), ('a', 3)]
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {'a': [1, 2, 3]})

    def test_min_max_values(self):
        min_val = -10
        max_val = 10
        data = list(zip(range(min_val, max_val + 1), range(min_val, max_val + 1)))
        result = grouping_dictionary(data)
        for k, v in result.items():
            self.assertGreaterEqual(min(v), min_val)
            self.assertLessEqual(max(v), max_val)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            grouping_dictionary([1, 2])
