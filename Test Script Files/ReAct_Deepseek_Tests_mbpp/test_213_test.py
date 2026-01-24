import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_strings(('abc', 'def'), ('ghi', 'jkl')), (('abcghi', 'defjkl'),))

    def test_empty_strings(self):
        self.assertEqual(concatenate_strings(('', ''), ('', '')), (('', ''),))

    def test_single_character_strings(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('c', 'd')), (('ac', 'bd'),))

    def test_long_strings(self):
        self.assertEqual(concatenate_strings(('abcdefgh', 'ijklmnop'), ('qrstuvwx', 'yz')), (('abcdefghqrstuvwx', 'ijklmnopyz'),))

    def test_mismatch_length_tuples(self):
        with self.assertRaises(ValueError):
            concatenate_strings(('abc', 'def', 'ghi'), ('jkl', 'mno'))

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate_strings(('abc', 123), ('def', 456))
