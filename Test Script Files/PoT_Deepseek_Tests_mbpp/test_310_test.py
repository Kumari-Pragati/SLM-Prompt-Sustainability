import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_tuple('hello world'), ('hello', 'world'))

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(''), ())

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple('   spacious   '), ('s', 'p', 'a', 'c', 'i', 'o', 'u', 's'))

    def test_string_with_no_spaces(self):
        self.assertEqual(string_to_tuple('nospaces'), ('n', 'o', 's', 'p', 'a', 'c', 'e', 's'))

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_tuple('special@#characters'), ('s', 'p', 'e', 'c', 'i', 'a', 'l', '@', '#', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's'))
