import unittest
from mbpp_475_code import Counter
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):

    def test_sort_counter(self):
        # Test with a dictionary
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        expected_output = [('c', 3), ('b', 2), ('a', 1)]
        self.assertEqual(sort_counter(dict1), expected_output)

        # Test with an empty dictionary
        dict1 = {}
        expected_output = []
        self.assertEqual(sort_counter(dict1), expected_output)

        # Test with a dictionary with one element
        dict1 = {'a': 1}
        expected_output = [('a', 1)]
        self.assertEqual(sort_counter(dict1), expected_output)

        # Test with a dictionary with duplicate values
        dict1 = {'a': 1, 'b': 1, 'c': 1}
        expected_output = [('c', 1), ('b', 1), ('a', 1)]
        self.assertEqual(sort_counter(dict1), expected_output)

        # Test with a dictionary with negative values
        dict1 = {'a': -1, 'b': -2, 'c': -3}
        expected_output = [('c', -3), ('b', -2), ('a', -1)]
        self.assertEqual(sort_counter(dict1), expected_output)
