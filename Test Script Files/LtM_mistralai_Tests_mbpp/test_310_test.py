import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(string_to_tuple("abc"), ("a", "b", "c"))

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_single_char_string(self):
        self.assertEqual(string_to_tuple("a"), ("a",))

    def test_space_only_string(self):
        self.assertEqual(string_to_tuple("   "), (" ",))

    def test_mixed_string(self):
        self.assertEqual(string_to_tuple("ab c d   e"), ("a", "b", "c", "d", "e"))
