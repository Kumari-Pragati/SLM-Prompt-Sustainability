import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_strings(('abc', 'def'), ('ghi', 'jkl')), (('abcghi', 'defjkl'),))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_strings((), ()), ((),))

    def test_single_element_tuples(self):
        self.assertEqual(concatenate_strings(('a',), ('b',)), (('ab',),))

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            concatenate_strings(('abc', 'def'), ('ghi',))

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate_strings(('abc', 123), ('ghi', 'jkl'))
