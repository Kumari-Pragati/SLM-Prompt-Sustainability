import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_ascii_value_normal(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('z'), 122)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('Z'), 90)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('9'), 57)

    def test_ascii_value_edge_cases(self):
        self.assertEqual(ascii_value(' '), 32)
        self.assertEqual(ascii_value('_'), 95)
        self.assertEqual(ascii_value('~'), 126)

    def test_ascii_value_invalid_input(self):
        self.assertRaises(ValueError, ascii_value, 123)
        self.assertRaises(ValueError, ascii_value, '')
