import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(ascii_value_string('a'), 97)

    def test_edge_condition(self):
        self.assertEqual(ascii_value_string(''), None)

    def test_boundary_condition(self):
        self.assertEqual(ascii_value_string(' '), 32)
        self.assertEqual(ascii_value_string('A'), 65)

    def test_complex_case(self):
        self.assertEqual(ascii_value_string('1'), 49)
        self.assertEqual(ascii_value_string('!'), 33)
