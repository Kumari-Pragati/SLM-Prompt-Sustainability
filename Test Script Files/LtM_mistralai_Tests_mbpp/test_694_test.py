import unittest
from mbpp_694_code import extract_unique

class TestExtractUnique(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(extract_unique({'a': ['a', 'b', 'c'], 'b': ['b', 'b', 'c']}), ['a', 'b', 'c'])
        self.assertEqual(extract_unique({'a': ['a'], 'b': ['b']}), ['a', 'b'])
        self.assertEqual(extract_unique({'a': ['a', 'a'], 'b': ['b', 'b']}), ['a', 'b'])

    def test_edge_cases(self):
        self.assertEqual(extract_unique({'a': [], 'b': ['b']}), ['b'])
        self.assertEqual(extract_unique({'a': ['a'], 'b': []}), ['a'])
        self.assertEqual(extract_unique({'a': ['a'], 'b': ['a']}), ['a'])

    def test_complex(self):
        self.assertEqual(extract_unique({'a': ['a', 'b', 'c'], 'b': ['b', 'c', 'a']}), ['a', 'b', 'c'])
        self.assertEqual(extract_unique({'a': ['a', 'b', 'c'], 'b': ['c', 'b', 'a']}), ['a', 'b', 'c'])
        self.assertEqual(extract_unique({'a': ['a', 'b', 'c'], 'b': ['c', 'a', 'b']}), ['a', 'b', 'c'])
