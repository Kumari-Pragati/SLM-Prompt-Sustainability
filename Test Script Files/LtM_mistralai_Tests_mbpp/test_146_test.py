import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(ascii_value_string('a'), 97)
        self.assertEqual(ascii_value_string('0'), 48)
        self.assertEqual(ascii_value_string('Z'), 90)
        self.assertEqual(ascii_value_string('9'), 57)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(ascii_value_string(''), 0)
        self.assertEqual(ascii_value_string(' '), 32)
        self.assertEqual(ascii_value_string('A'), 65)
        self.assertEqual(ascii_value_string('aA'), 97 + 65)
        self.assertEqual(ascii_value_string('z'), 122)
        self.assertEqual(ascii_value_string('Zz'), 90 + 122)

    def test_complex_and_corner_cases(self):
        self.assertEqual(ascii_value_string('A-B'), 65 + 97)
        self.assertEqual(ascii_value_string('12345'), 49 + 50 + 51 + 52 + 53)
        self.assertEqual(ascii_value_string('!@#$%^&*()_+-=[]{}|;:,.<>?'),
                        33 + 34 + 35 + 36 + 37 + 38 + 39 + 40 + 41 + 42 + 43 + 44 + 45 + 46 + 47 + 48 + 49 + 50 + 51 + 52 + 53 + 54 + 55 + 56 + 57 + 58 + 59 + 60 + 61 + 62)
