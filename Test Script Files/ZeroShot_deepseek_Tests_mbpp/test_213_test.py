import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(concatenate_strings(('abc', 'def'), ('ghi', 'jkl')), (('abcghi', 'defjkl'),))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_strings((), ()), ((),))

    def test_different_lengths(self):
        self.assertEqual(concatenate_strings(('abc', 'def', 'ghi'), ('jkl', 'mno')), (('abcjkl', 'defmno'),))

    def test_with_integers(self):
        self.assertEqual(concatenate_strings((123, 456), (789, 0)), (('123789', '4560'),))

    def test_with_mixed_types(self):
        self.assertEqual(concatenate_strings(('abc', 123), (456, 'def')), (('abc456', '123def'),))
