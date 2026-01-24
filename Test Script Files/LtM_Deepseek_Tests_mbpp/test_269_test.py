import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_ascii_value_simple(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('0'), 48)

    def test_ascii_value_edge(self):
        self.assertEqual(ascii_value(' '), 32)
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value('\t'), 9)

    def test_ascii_value_boundary(self):
        self.assertEqual(ascii_value('~'), 126)
        self.assertEqual(ascii_value('`'), 96)
        self.assertEqual(ascii_value('\u007f'), 127)

    def test_ascii_value_complex(self):
        self.assertEqual(ascii_value('é'), 233)
        self.assertEqual(ascii_value('漢'), 26385)
