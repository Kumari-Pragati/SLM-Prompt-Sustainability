import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_char('hello'), 'l')
        self.assertEqual(max_char('world'), 'l')
        self.assertEqual(max_char('abc'), 'b')
        self.assertEqual(max_char('xyz'), 'x')

    def test_empty(self):
        self.assertEqual(max_char(''), '')

    def test_single_char(self):
        self.assertEqual(max_char('a'), 'a')
        self.assertEqual(max_char('b'), 'b')
        self.assertEqual(max_char('c'), 'c')

    def test_multiple_chars(self):
        self.assertEqual(max_char('hello world'), 'o')
        self.assertEqual(max_char('abc def'), 'd')

    def test_non_ascii(self):
        self.assertEqual(max_char('hello, world!'), 'o')
        self.assertEqual(max_char('abc, def!'), 'd')

    def test_spaces(self):
        self.assertEqual(max_char('hello world'), 'o')
        self.assertEqual(max_char('abc def'), 'd')

    def test_punctuation(self):
        self.assertEqual(max_char('hello, world!'), 'o')
        self.assertEqual(max_char('abc, def!'), 'd')
