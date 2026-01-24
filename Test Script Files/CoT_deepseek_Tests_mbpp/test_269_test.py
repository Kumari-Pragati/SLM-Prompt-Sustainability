import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_single_character_string(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('!'), 33)

    def test_empty_string(self):
        self.assertEqual(ascii_value(''), None)

    def test_multiple_characters(self):
        self.assertEqual(ascii_value('ab'), None)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
        with self.assertRaises(TypeError):
            ascii_value(True)
        with self.assertRaises(TypeError):
            ascii_value(None)
