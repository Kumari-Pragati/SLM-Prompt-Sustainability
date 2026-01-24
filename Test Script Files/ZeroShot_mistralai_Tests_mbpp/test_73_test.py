import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(multiple_split(''), [])

    def test_single_space(self):
        self.assertEqual(multiple_split(' a '), ['a'])

    def test_single_comma(self):
        self.assertEqual(multiple_split('a,b'), ['a', 'b'])

    def test_single_semicolon(self):
        self.assertEqual(multiple_split('a;b'), ['a', 'b'])

    def test_single_asterisk(self):
        self.assertEqual(multiple_split('a*b'), ['a', 'b'])

    def test_single_newline(self):
        self.assertEqual(multiple_split('a\nb'), ['a', 'b'])

    def test_multiple_delimiters(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_escaped_delimiters(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a,b;c*d\ne'])

    def test_trailing_delimiter(self):
        self.assertEqual(multiple_split('a;'), ['a'])

    def test_leading_delimiter(self):
        self.assertEqual(multiple_split(';a'), [])

    def test_multiple_spaces(self):
        self.assertEqual(multiple_split(' a b '), ['a', 'b'])

    def test_multiple_whitespace_delimiters(self):
        self.assertEqual(multiple_split(' a, b ; c '), ['a', 'b', 'c'])
