import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(extract_unique({}), [])

    def test_single_value(self):
        self.assertEqual(extract_unique({'a': [1]}), [1])

    def test_multiple_values(self):
        self.assertEqual(extract_unique({'a': [1, 2], 'b': [2, 3]}), [1, 2, 3])

    def test_duplicates(self):
        self.assertEqual(extract_unique({'a': [1, 1, 2]}), [1, 2])

    def test_empty_values(self):
        self.assertEqual(extract_unique({'a': [], 'b': [1]}), [1])

    def test_negative_values(self):
        self.assertEqual(extract_unique({'a': [-1, 0, 1]}), [-1, 0, 1])

    def test_large_values(self):
        self.assertEqual(extract_unique({'a': [1000, 2000, 3000]}), [1000, 2000, 3000])

    def test_mixed_types(self):
        self.assertEqual(extract_unique({'a': [1, 'a', 2.5]}), [1, 2.5, 'a'])
