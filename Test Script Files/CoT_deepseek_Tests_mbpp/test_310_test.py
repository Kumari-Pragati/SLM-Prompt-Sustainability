import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_tuple('hello world'), ('hello', 'world'))

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(''), ())

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple('   '), ())

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_tuple('!@#$%^&*()'), ('!@#$%^&*()',))

    def test_string_with_numbers(self):
        self.assertEqual(string_to_tuple('1234567890'), ('1234567890',))

    def test_string_with_mixed_characters(self):
        self.assertEqual(string_to_tuple('h3ll0 W0r1d'), ('h3ll0', 'W0r1d'))
