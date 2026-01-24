import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_typical_case(self):
        arr = ['flower', 'flow', 'flight']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'fl')

    def test_single_string(self):
        arr = ['hello']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'hello')

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), '')

    def test_different_prefixes(self):
        arr = ['dog', 'racecar', 'car']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), '')

    def test_same_prefixes(self):
        arr = ['apple', 'appetizer', 'application']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'app')

    def test_empty_strings(self):
        arr = ['', 'hello', '']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), '')

    def test_large_input(self):
        arr = ['abcdefgh', 'abcdefg', 'abcdef']
        n = len(arr)
        self.assertEqual(common_prefix(arr, n), 'abcdefgh')
