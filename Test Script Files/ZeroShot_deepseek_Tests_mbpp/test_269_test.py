import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_ascii_value(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('1'), 49)
        self.assertEqual(ascii_value(' '), 32)
        self.assertEqual(ascii_value('!'), 33)
