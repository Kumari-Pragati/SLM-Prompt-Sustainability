import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_tuple(''), ())

    def test_string_with_spaces(self):
        self.assertEqual(string_to_tuple('   '), ())

    def test_string_without_spaces(self):
        self.assertEqual(string_to_tuple('abc'), ('a', 'b', 'c'))

    def test_string_with_mixed_characters(self):
        self.assertEqual(string_to_tuple('a b c'), ('a', 'b', 'c'))

    def test_string_with_numbers(self):
        self.assertEqual(string_to_tuple('123'), ('1', '2', '3'))

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_tuple('!@#'), ('!', '@', '#'))
