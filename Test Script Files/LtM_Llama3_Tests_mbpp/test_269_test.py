import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('9'), 57)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(ascii_value(''), 0)
        self.assertEqual(ascii_value(' '), 32)
        self.assertEqual(ascii_value('\t'), 9)
        self.assertEqual(ascii_value('\n'), 10)
        self.assertEqual(ascii_value('\r'), 13)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ascii_value(None)
        with self.assertRaises(TypeError):
            ascii_value(123)
