import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('0'), 48)

    def test_edge_cases(self):
        self.assertEqual(ascii_value(' '), 32)
        self.assertEqual(ascii_value('\t'), 9)

    def test_special_cases(self):
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value('#'), 35)
        self.assertEqual(ascii_value('['), 91)
        self.assertEqual(ascii_value(']'), 93)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
        with self.assertRaises(TypeError):
            ascii_value(None)
        with self.assertRaises(TypeError):
            ascii_value(True)
        with self.assertRaises(TypeError):
            ascii_value([])
        with self.assertRaises(TypeError):
            ascii_value({})
