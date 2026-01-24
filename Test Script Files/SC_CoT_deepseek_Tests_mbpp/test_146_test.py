import unittest

from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ascii_value_string('a'), 97)

    def test_edge_case(self):
        self.assertEqual(ascii_value_string(''), None)

    def test_special_case(self):
        self.assertEqual(ascii_value_string(' '), 32)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            ascii_value_string(123)
