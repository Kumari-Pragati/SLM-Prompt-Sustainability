import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):
    def test_typical(self):
        self.assertListEqual(extract_unique({'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [1, 2, 3, 4]}), [1, 2, 3, 4])
        self.assertListEqual(extract_unique({'a': [1, 1, 2, 3], 'b': [2, 2, 3, 4], 'c': [1, 2, 3, 4]}), [1, 2, 3])

    def test_edge_and_boundary(self):
        self.assertListEqual(extract_unique({'a': [], 'b': [2, 3], 'c': [1, 2, 3, 4]}), [2, 3])
        self.assertListEqual(extract_unique({'a': [1], 'b': [2, 3], 'c': [1, 2, 3, 4]}), [1, 2, 3])
        self.assertListEqual(extract_unique({'a': [1, 1], 'b': [2, 3], 'c': [1, 2, 3, 4]}), [1, 2, 3])
