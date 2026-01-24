import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):

    def test_simple_input(self):
        test_dict = {'a': [1, 2, 3], 'b': [2, 3, 4]}
        self.assertEqual(extract_unique(test_dict), [1, 2, 3, 4])

    def test_empty_input(self):
        test_dict = {}
        self.assertEqual(extract_unique(test_dict), [])

    def test_single_value_input(self):
        test_dict = {'a': [5]}
        self.assertEqual(extract_unique(test_dict), [5])

    def test_duplicate_values(self):
        test_dict = {'a': [1, 2, 2], 'b': [2, 3, 3]}
        self.assertEqual(extract_unique(test_dict), [1, 2, 3])

    def test_negative_values(self):
        test_dict = {'a': [-1, -2, -3], 'b': [-2, -3, -4]}
        self.assertEqual(extract_unique(test_dict), [-1, -2, -3, -4])

    def test_mixed_values(self):
        test_dict = {'a': [1, -2, 3], 'b': [-2, 3, 4]}
        self.assertEqual(extract_unique(test_dict), [1, -2, 3, 4])
