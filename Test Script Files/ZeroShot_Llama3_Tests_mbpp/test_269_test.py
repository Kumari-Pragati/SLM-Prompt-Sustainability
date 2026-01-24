import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):

    def test_ascii_value(self):
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value(''), None)
        self.assertEqual(ascii_value(None), None)

    def test_ascii_value_type_error(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
