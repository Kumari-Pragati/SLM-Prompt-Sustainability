import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_typical_use_case(self):
        dict1 = {'a': 3, 'b': 2, 'c': 1}
        expected_output = [('a', 3), ('b', 2), ('c', 1)]
        self.assertEqual(sort_counter(dict1), expected_output)

    def test_empty_dict(self):
        dict1 = {}
        expected_output = []
        self.assertEqual(sort_counter(dict1), expected_output)

    def test_single_key_dict(self):
        dict1 = {'a': 1}
        expected_output = [('a', 1)]
        self.assertEqual(sort_counter(dict1), expected_output)

    def test_multiple_keys_dict(self):
        dict1 = {'a': 3, 'b': 2, 'c': 1, 'd': 4, 'e': 5}
        expected_output = [('e', 5), ('d', 4), ('a', 3), ('b', 2), ('c', 1)]
        self.assertEqual(sort_counter(dict1), expected_output)

    def test_dict_with_duplicates(self):
        dict1 = {'a': 3, 'b': 2, 'c': 1, 'a': 2}
        expected_output = [('a', 3), ('a', 2), ('b', 2), ('c', 1)]
        self.assertEqual(sort_counter(dict1), expected_output)
