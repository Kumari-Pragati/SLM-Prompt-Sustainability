import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):

    def test_extract_unique(self):
        test_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
        self.assertEqual(extract_unique(test_dict), [1, 2, 3, 4, 5])

    def test_extract_unique_empty_dict(self):
        test_dict = {}
        self.assertEqual(extract_unique(test_dict), [])

    def test_extract_unique_single_value(self):
        test_dict = {'a': [1]}
        self.assertEqual(extract_unique(test_dict), [1])

    def test_extract_unique_multiple_values(self):
        test_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5, 6]}
        self.assertEqual(extract_unique(test_dict), [1, 2, 3, 4, 5, 6])

    def test_extract_unique_empty_list(self):
        test_dict = {'a': []}
        self.assertEqual(extract_unique(test_dict), [])
