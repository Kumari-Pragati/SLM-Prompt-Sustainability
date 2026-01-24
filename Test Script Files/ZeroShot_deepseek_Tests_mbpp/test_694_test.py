import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(extract_unique({}), [])

    def test_single_value(self):
        self.assertEqual(extract_unique({'a': [1]}), [1])

    def test_multiple_values(self):
        self.assertEqual(extract_unique({'a': [1, 2, 3], 'b': [2, 3, 4]}), [1, 2, 3, 4])

    def test_duplicates(self):
        self.assertEqual(extract_unique({'a': [1, 2, 2], 'b': [2, 3, 4]}), [1, 2, 3, 4])

    def test_mixed_types(self):
        self.assertEqual(extract_unique({'a': [1, '2', 3], 'b': ['2', 3, 4]}), [1, '2', 3, 4])
