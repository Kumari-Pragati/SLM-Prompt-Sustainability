import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('!'), 33)

    def test_edge(self):
        self.assertEqual(ascii_value(''), 0)
        self.assertEqual(ascii_value(' '), 32)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            ascii_value(None)
        with self.assertRaises(TypeError):
            ascii_value(123)
