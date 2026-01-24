import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):

    def test_simple_word(self):
        self.assertEqual(split('hello'), ['h', 'e', 'l', 'l', 'o'])

    def test_empty_word(self):
        self.assertEqual(split(''), [])

    def test_special_characters(self):
        self.assertEqual(split('!@#$%^&*()'), ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'])

    def test_numbers(self):
        self.assertEqual(split('1234567890'), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

    def test_whitespace(self):
        self.assertEqual(split(' '), [' '])

    def test_long_word(self):
        self.assertEqual(split('abcdefghijklmnopqrstuvwxyz'), 
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
