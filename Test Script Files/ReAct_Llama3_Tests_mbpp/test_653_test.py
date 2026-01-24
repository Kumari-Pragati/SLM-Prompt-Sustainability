import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(grouping_dictionary([]), {})

    def test_single_element_list(self):
        self.assertEqual(grouping_dictionary([(1, 'a')]), {1: ['a']})

    def test_multiple_elements_list(self):
        self.assertEqual(grouping_dictionary([(1, 'a'), (1, 'b'), (2, 'c')]), {1: ['a', 'b'], 2: ['c']})

    def test_empty_key(self):
        with self.assertRaises(TypeError):
            grouping_dictionary([(None, 'a')])

    def test_non_list_value(self):
        with self.assertRaises(TypeError):
            grouping_dictionary([(1, 'a'), (1, 'b'), (1, 'c')])

    def test_mixed_types(self):
        self.assertEqual(grouping_dictionary([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]), {1: ['a'], 2: ['b'], 3: ['c'], 4: ['d']})
