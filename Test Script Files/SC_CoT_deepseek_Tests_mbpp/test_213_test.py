import unittest

from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_strings(('abc', 'def'), ('ghi', 'jkl')), (('abcghi', 'defjkl'),))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_strings((), ()), ((),))

    def test_one_empty_tuple(self):
        self.assertEqual(concatenate_strings(('abc', 'def'), ()), ((),))
        self.assertEqual(concatenate_strings((), ('ghi', 'jkl')), ((),))

    def test_single_string_tuples(self):
        self.assertEqual(concatenate_strings(('abc',), ('ghi',)), (('abcghi',),))

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            concatenate_strings(('abc', 'def', 'ghi'), ('jkl',))
