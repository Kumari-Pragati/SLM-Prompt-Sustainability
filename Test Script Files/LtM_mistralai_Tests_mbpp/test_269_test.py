import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_simple_ascii(self):
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('0'), 48)

    def test_edge_cases(self):
        self.assertEqual(ascii_value('Z'), 90)
        self.assertEqual(ascii_value('z'), 122)
        self.assertEqual(ascii_value('9'), 57)
        self.assertEqual(ascii_value(' '), 32)

    def test_complex_cases(self):
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value('_'), 95)
        self.assertEqual(ascii_value('ö'), 246)  # Assuming the function handles non-ASCII characters
