import unittest
from mbpp_653_code import defaultdict
from six.moves import range

from653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_normal_case(self):
        data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {'a': [1, 2], 'b': [3, 4]})

    def test_edge_case_empty_list(self):
        data = []
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {})

    def test_edge_case_single_item(self):
        data = [('a', 1)]
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {'a': [1]})

    def test_edge_case_single_key(self):
        data = [('a', 1), ('a', 1)]
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {'a': [1, 1]})

    def test_edge_case_duplicate_value(self):
        data = [('a', 1), ('a', 1), ('b', 2), ('b', 2)]
        result = grouping_dictionary(data)
        self.assertDictEqual(result, {'a': [1, 1], 'b': [2, 2]})

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            grouping_dictionary(123)

    def test_invalid_input_type_key_value(self):
        with self.assertRaises(TypeError):
            grouping_dictionary([(1, 2), (3, 4)])
