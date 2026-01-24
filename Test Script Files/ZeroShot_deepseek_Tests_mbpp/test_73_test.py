import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_comma_separated(self):
        self.assertEqual(multiple_split('a,b,c'), ['a', 'b', 'c'])

    def test_semicolon_separated(self):
        self.assertEqual(multiple_split('a;b;c'), ['a', 'b', 'c'])

    def test_star_separated(self):
        self.assertEqual(multiple_split('a*b*c'), ['a', 'b', 'c'])

    def test_newline_separated(self):
        self.assertEqual(multiple_split('a\nb\nc'), ['a', 'b', 'c'])

    def test_mixed_separators(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_empty_string(self):
        self.assertEqual(multiple_split(''), [])

    def test_single_character(self):
        self.assertEqual(multiple_split('a'), ['a'])
