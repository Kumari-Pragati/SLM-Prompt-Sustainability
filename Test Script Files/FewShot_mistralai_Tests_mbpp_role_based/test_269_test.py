import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_valid_ascii_characters(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('Z'), 90)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('9'), 57)

    def test_invalid_input(self):
        self.assertRaises(ValueError, ascii_value, 123)
        self.assertRaises(ValueError, ascii_value, '')
        self.assertRaises(ValueError, ascii_value, None)
