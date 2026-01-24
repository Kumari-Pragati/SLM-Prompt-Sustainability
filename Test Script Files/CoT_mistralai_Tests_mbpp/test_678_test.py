import unittest
from mbpp_678_code import str
from six.moves.string_types import StringIO

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_spaces(' '), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces('  abc  '), 'abc')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces('  abc  '), 'abc')
        self.assertEqual(remove_spaces('abc  '), 'abc')
        self.assertEqual(remove_spaces(' abc '), 'abc')

    def test_mixed_case(self):
        self.assertEqual(remove_spaces('AbC dEf 123'), 'AbCdEf123')

    def test_punctuation_and_spaces(self):
        self.assertEqual(remove_spaces('Hello, World!'), 'HelloWorld')
        self.assertEqual(remove_spaces('Hello, World!   '), 'HelloWorld')

    def test_multiple_words_and_punctuation(self):
        self.assertEqual(remove_spaces('Hello, World!   It is a beautiful day.'), 'HelloWorldItIsABeautifulDay')

    def test_tab_spaces(self):
        self.assertEqual(remove_spaces('\tHello\tWorld'), 'HelloWorld')

    def test_unicode_string(self):
        with StringIO('Héllo Wórld') as unicode_str:
            self.assertEqual(remove_spaces(unicode_str.read()), 'HlloWld')

    def test_invalid_input(self):
        self.assertRaises(TypeError, remove_spaces, 123)
