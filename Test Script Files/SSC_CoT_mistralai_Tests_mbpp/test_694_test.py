import unittest
from mbpp_694_code import range
from collections import defaultdict
from 694_code import extract_unique

class TestExtractUnique(unittest.TestCase):

    def test_normal_input(self):
        test_dict = {
            'a': [1, 2, 3],
            'b': [3, 2, 1],
            'c': [4, 4, 4, 5]
        }
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(extract_unique(test_dict), expected)

    def test_empty_input(self):
        test_dict = {}
        self.assertEqual(extract_unique(test_dict), [])

    def test_single_value_input(self):
        test_dict = {'a': [1]}
        expected = [1]
        self.assertEqual(extract_unique(test_dict), expected)

    def test_duplicate_values(self):
        test_dict = {'a': [1, 1, 2, 2], 'b': [3, 3, 3]}
        expected = [1, 2, 3]
        self.assertEqual(extract_unique(test_dict), expected)

    def test_mixed_types(self):
        test_dict = {'a': [1, 2, 3], 'b': [3, 2, 'two', 1], 'c': [4, 4, 4, 5]}
        expected = [1, 2, 3, 4, 5, 'two']
        self.assertEqual(extract_unique(test_dict), expected)

    def test_negative_numbers(self):
        test_dict = {'a': [-1, 0, 1], 'b': [-3, -2, -1]}
        expected = [-3, -2, -1, 0, 1]
        self.assertEqual(extract_unique(test_dict), expected)

    def test_large_numbers(self):
        test_dict = {'a': [1000000001, 1000000002, 1000000003], 'b': [1000000004, 1000000005]}
        expected = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
        self.assertEqual(extract_unique(test_dict), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_unique({1: [2, 3], 2: [4, 5]})
