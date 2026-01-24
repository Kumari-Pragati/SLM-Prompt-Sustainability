import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_simple_concatenation(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('c', 'd')), ('ac', 'bd'))

    def test_concatenation_with_empty_tuples(self):
        self.assertEqual(concatenate_strings((), ('x', 'y')), ())
        self.assertEqual(concatenate_strings(('a',), ()), ('a',))

    def test_concatenation_with_different_length_tuples(self):
        self.assertEqual(concatenate_strings(('a', 'b', 'c'), ('d',)), ('ad', 'bc'))
        self.assertEqual(concatenate_strings(('a', 'b'), ('c', 'd', 'e')), ('ac', 'bd'))

    def test_concatenation_with_special_characters(self):
        self.assertEqual(concatenate_strings(('!', '@'), ('#', '$')), ('!#', '@$'))
        self.assertEqual(concatenate_strings(('a', 'b'), ('!', '@')), ('a!', 'b@'))
