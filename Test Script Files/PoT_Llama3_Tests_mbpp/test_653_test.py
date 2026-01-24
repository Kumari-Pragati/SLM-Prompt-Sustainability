import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(grouping_dictionary([(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]), {1: ['a', 'c'], 2: ['b'], 3: ['d']})

    def test_edge_case_empty_input(self):
        self.assertEqual(grouping_dictionary([]), {})

    def test_edge_case_single_element_input(self):
        self.assertEqual(grouping_dictionary([(1, 'a')]), {1: ['a']})

    def test_edge_case_duplicates(self):
        self.assertEqual(grouping_dictionary([(1, 'a'), (1, 'b'), (2, 'c')]), {1: ['a', 'b'], 2: ['c']})

    def test_edge_case_single_key(self):
        self.assertEqual(grouping_dictionary([(1, 'a'), (1, 'b'), (1, 'c')]), {1: ['a', 'b', 'c']})

    def test_edge_case_single_value(self):
        self.assertEqual(grouping_dictionary([(1, 'a'), (1, 'a'), (1, 'a')]), {1: ['a', 'a', 'a']})
