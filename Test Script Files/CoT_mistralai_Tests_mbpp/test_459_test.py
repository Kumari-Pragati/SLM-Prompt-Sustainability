import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_single_uppercase(self):
        self.assertEqual(remove_uppercase('A'), '')

    def test_single_lowercase(self):
        self.assertEqual(remove_uppercase('a'), 'a')

    def test_multiple_uppercase(self):
        self.assertEqual(remove_uppercase('ABC'), 'c')

    def test_multiple_lowercase(self):
        self.assertEqual(remove_uppercase('abc'), 'abc')

    def test_mixed_case(self):
        self.assertEqual(remove_uppercase('AbCdEf'), 'cd')

    def test_leading_trailing_uppercase(self):
        self.assertEqual(remove_uppercase('ABCabcDEF'), 'abcdef')

    def test_leading_trailing_whitespace(self):
        self.assertEqual(remove_uppercase(' ABC ABC '), '   ')

    def test_punctuation_and_uppercase(self):
        self.assertEqual(remove_uppercase('Hello, World!'), 'hello, world!')

    def test_invalid_input_non_string(self):
        self.assertRaises(TypeError, remove_uppercase, 123)
