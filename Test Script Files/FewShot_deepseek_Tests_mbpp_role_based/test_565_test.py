import unittest
from mbpp_565_code import split

class TestSplit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(split('hello'), ['h', 'e', 'l', 'l', 'o'])

    def test_empty_string(self):
        self.assertEqual(split(''), [])

    def test_single_character(self):
        self.assertEqual(split('a'), ['a'])

    def test_special_characters(self):
        self.assertEqual(split('!@#'), ['!', '@', '#'])

    def test_numbers(self):
        self.assertEqual(split('12345'), ['1', '2', '3', '4', '5'])

    def test_whitespace(self):
        self.assertEqual(split(' '), [' '])

    def test_multiple_whitespace(self):
        self.assertEqual(split('   '), [' ', ' ', ' '])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            split(None)
