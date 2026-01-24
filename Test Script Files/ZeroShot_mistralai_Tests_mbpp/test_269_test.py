import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_ascii_value_lowercase_letters(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('b'), 98)
        self.assertEqual(ascii_value('z'), 122)

    def test_ascii_value_uppercase_letters(self):
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('B'), 66)
        self.assertEqual(ascii_value('Z'), 90)

    def test_ascii_value_numbers(self):
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('1'), 49)
        self.assertEqual(ascii_value('9'), 57)

    def test_ascii_value_special_characters(self):
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value('@'), 64)
        self.assertEqual(ascii_value('_'), 95)

    def test_ascii_value_empty_string(self):
        self.assertEqual(ascii_value(''), 0)
