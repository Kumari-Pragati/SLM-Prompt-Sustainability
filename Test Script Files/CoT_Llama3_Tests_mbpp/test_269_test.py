import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_ascii_value(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value(''), 0)

    def test_edge_cases(self):
        self.assertEqual(ascii_value(''), 0)
        self.assertEqual(ascii_value('\n'), 10)
        self.assertEqual(ascii_value('\t'), 9)
        self.assertEqual(ascii_value('\r'), 13)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ascii_value(None)
        with self.assertRaises(TypeError):
            ascii_value(123)
