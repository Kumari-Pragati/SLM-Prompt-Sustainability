import unittest
from mbpp_653_code import defaultdict
from mbpp_653_code import grouping_dictionary

class TestGroupingDictionary(unittest.TestCase):

    def test_grouping_dictionary(self):
        # Test with a list of tuples
        l = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
        expected_output = defaultdict(list, {'a': [1, 3], 'b': [2, 4], 'c': [5]})
        self.assertEqual(grouping_dictionary(l), expected_output)

        # Test with an empty list
        l = []
        expected_output = defaultdict(list)
        self.assertEqual(grouping_dictionary(l), expected_output)

        # Test with a list containing one tuple
        l = [('a', 1)]
        expected_output = defaultdict(list, {'a': [1]})
        self.assertEqual(grouping_dictionary(l), expected_output)

        # Test with a list containing duplicate keys
        l = [('a', 1), ('a', 2), ('a', 3)]
        expected_output = defaultdict(list, {'a': [1, 2, 3]})
        self.assertEqual(grouping_dictionary(l), expected_output)
