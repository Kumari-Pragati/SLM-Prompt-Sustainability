import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(ascii_value_string('a'), 97)
        self.assertEqual(ascii_value_string('A'), 65)
        self.assertEqual(ascii_value_string('1'), 49)

    def test_edge_cases(self):
        self.assertEqual(ascii_value_string(''), None)

    def test_corner_cases(self):
        self.assertEqual(ascii_value_string(' '), 32)
        self.assertEqual(ascii_value_string('!'), 33)
        self.assertEqual(ascii_value_string('@'), 64)
