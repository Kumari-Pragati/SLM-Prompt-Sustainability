import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('Z'), 90)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('9'), 57)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(ascii_value(' '), 32)
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value('~'), 126)

    def test_special_characters(self):
        self.assertEqual(ascii_value('@'), 64)
        self.assertEqual(ascii_value('#'), 35)
        self.assertEqual(ascii_value('$'), 36)

    def test_invalid_input(self):
        self.assertRaises(ValueError, ascii_value, 123)
        self.assertRaises(ValueError, ascii_value, None)
        self.assertRaises(ValueError, ascii_value, '')
