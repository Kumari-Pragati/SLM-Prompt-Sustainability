import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_single_space(self):
        self.assertEqual(string_to_tuple(" "), ())

    def test_multiple_spaces(self):
        self.assertEqual(string_to_tuple("   "), ())

    def test_single_non_space(self):
        self.assertEqual(string_to_tuple("a"), ('a',))

    def test_multiple_non_spaces(self):
        self.assertEqual(string_to_tuple("abc"), ('abc',))

    def test_mixed_spaces_and_non_spaces(self):
        self.assertEqual(string_to_tuple("a b c"), ('a', 'c'))

    def test_string_with_leading_spaces(self):
        self.assertEqual(string_to_tuple("   abc"), ('abc',))

    def test_string_with_trailing_spaces(self):
        self.assertEqual(string_to_tuple("abc   "), ('abc',))

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(string_to_tuple("   abc   "), ('abc',))

    def test_string_with_multiple_leading_and_trailing_spaces(self):
        self.assertEqual(string_to_tuple("   abc   "), ('abc',))
