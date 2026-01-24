import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_ascii_value_string(self):
        self.assertEqual(ascii_value_string('a'), 97)
        self.assertEqual(ascii_value_string('A'), 65)
        self.assertEqual(ascii_value_string('1'), 49)
        self.assertEqual(ascii_value_string('!'), 33)
        self.assertEqual(ascii_value_string(''), None)
        self.assertEqual(ascii_value_string('abc'), 97)
        self.assertEqual(ascii_value_string('ABC'), 65)
        self.assertEqual(ascii_value_string('123'), 49)
        self.assertEqual(ascii_value_string('!@#'), 33)

    def test_edge_cases(self):
        self.assertEqual(ascii_value_string(''), None)
        self.assertEqual(ascii_value_string(''), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ascii_value_string(123)
