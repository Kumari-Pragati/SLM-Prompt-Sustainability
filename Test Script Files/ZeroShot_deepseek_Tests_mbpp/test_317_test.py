import unittest
from mbpp_317_code import groupby
from mbpp_317_code import modified_encode

class TestModifiedEncode(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(modified_encode(['a']), ['a'])

    def test_multiple_same_elements(self):
        self.assertEqual(modified_encode(['a', 'a', 'a']), [[3, 'a']])

    def test_multiple_different_elements(self):
        self.assertEqual(modified_encode(['a', 'b', 'a']), [['a'], ['b'], ['a']])

    def test_empty_list(self):
        self.assertEqual(modified_encode([]), [])

    def test_large_list(self):
        self.assertEqual(modified_encode(['a']*10000 + ['b']), [[10000, 'a'], 'b'])
