import unittest
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_grouping_dictionary(self):
        self.assertEqual(grouping_dictionary([('a', 1), ('a', 2), ('b', 3), ('c', 4)]), 
                         {'a': [1, 2], 'b': [3], 'c': [4]})
        self.assertEqual(grouping_dictionary([('a', 1), ('b', 2), ('a', 3), ('c', 4)]), 
                         {'a': [1, 3], 'b': [2], 'c': [4]})
        self.assertEqual(grouping_dictionary([('a', 1), ('a', 2), ('a', 3), ('a', 4)]), 
                         {'a': [1, 2, 3, 4]})
        self.assertEqual(grouping_dictionary([]), {})

    def test_grouping_dictionary_empty_key(self):
        self.assertEqual(grouping_dictionary([('a', 1), ('', 2), ('b', 3), ('c', 4)]), 
                         {'a': [1], '': [2], 'b': [3], 'c': [4]})

    def test_grouping_dictionary_empty_value(self):
        self.assertEqual(grouping_dictionary([('a', None), ('b', None), ('c', None)]), 
                         {'a': [None], 'b': [None], 'c': [None]})
