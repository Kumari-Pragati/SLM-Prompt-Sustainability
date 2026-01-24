import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(grouping_dictionay([]), {})

    def test_single_item(self):
        self.assertDictEqual(grouping_dictionary([('a', 1)]), {'a': [1]})

    def test_multiple_items(self):
        self.assertDictEqual(grouping_dictionary([('a', 1), ('b', 2), ('a', 3)]), {'a': [1, 3], 'b': [2]})

    def test_duplicate_keys(self):
        self.assertDictEqual(grouping_dictionary([('a', 1), ('a', 2), ('b', 3)]), {'a': [1, 2], 'b': [3]})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            grouping_dictionary([(1, 2), ('a', 3)])
