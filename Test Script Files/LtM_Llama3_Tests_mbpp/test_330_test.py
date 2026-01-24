import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_char("Hello World"), ['World'])
        self.assertEqual(find_char("Python is fun"), ['fun'])
        self.assertEqual(find_char("Hello"), [])

    def test_edge(self):
        self.assertEqual(find_char(""), [])
        self.assertEqual(find_char("a"), [])
        self.assertEqual(find_char("abc"), [])

    def test_boundary(self):
        self.assertEqual(find_char("abcde"), ['abc', 'de'])
        self.assertEqual(find_char("abcdef"), ['abcdef'])

    def test_complex(self):
        self.assertEqual(find_char("Hello World, Python is fun!"), ['World', 'fun'])
        self.assertEqual(find_char("Python is fun, programming is awesome!"), ['fun', 'awesome'])
