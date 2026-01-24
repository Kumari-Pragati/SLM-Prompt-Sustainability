import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'a': [1, 2, 3], 'b': [2, 3, 4]}
        self.assertEqual(extract_unique(test_dict), [1, 2, 3, 4])

    def test_empty_dict(self):
        test_dict = {}
        self.assertEqual(extract_unique(test_dict), [])

    def test_single_value(self):
        test_dict = {'a': [1]}
        self.assertEqual(extract_unique(test_dict), [1])

    def test_duplicate_values(self):
        test_dict = {'a': [1, 1, 2, 2], 'b': [2, 3, 4, 4]}
        self.assertEqual(extract_unique(test_dict), [1, 2, 3, 4])

    def test_negative_numbers(self):
        test_dict = {'a': [-1, -2, -3], 'b': [-2, -3, -4]}
        self.assertEqual(extract_unique(test_dict), [-1, -2, -3, -4])

    def test_mixed_numbers(self):
        test_dict = {'a': [-1, 0, 1], 'b': [0, 1, 2]}
        self.assertEqual(extract_unique(test_dict), [-1, 0, 1, 2])

    def test_large_numbers(self):
        test_dict = {'a': [1000, 2000, 3000], 'b': [2000, 3000, 4000]}
        self.assertEqual(extract_unique(test_dict), [1000, 2000, 3000, 4000])
