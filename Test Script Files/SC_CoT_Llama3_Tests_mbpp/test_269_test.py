import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_typical_inputs(self):
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
        self.assertEqual(ascii_value('\x00'), 0)

    def test_special_and_corner_cases(self):
        self.assertEqual(ascii_value('!'), 33)
        self.assertEqual(ascii_value('@'), 64)
        self.assertEqual(ascii_value('#'), 35)
        self.assertEqual(ascii_value('$'), 36)
        self.assertEqual(ascii_value('%'), 37)
        self.assertEqual(ascii_value('^'), 94)
        self.assertEqual(ascii_value('&'), 38)
        self.assertEqual(ascii_value('*', 39))
        self.assertEqual(ascii_value('(', 40))
        self.assertEqual(ascii_value(')'), 41)
        self.assertEqual(ascii_value('[', 91))
        self.assertEqual(ascii_value(']', 93))
        self.assertEqual(ascii_value('{', 123))
        self.assertEqual(ascii_value('}', 125))
        self.assertEqual(ascii_value('<', 60))
        self.assertEqual(ascii_value('>', 62))
        self.assertEqual(ascii_value(',', 44))
        self.assertEqual(ascii_value('.', 46))
        self.assertEqual(ascii_value('?', 63))
        self.assertEqual(ascii_value('/', 47))
        self.assertEqual(ascii_value('\\', 92))
        self.assertEqual(ascii_value('|', 124))
        self.assertEqual(ascii_value('"', 34))
        self.assertEqual(ascii_value("'", 39))
        self.assertEqual(ascii_value('`', 96))
        self.assertEqual(ascii_value('\'', 39))
        self.assertEqual(ascii_value('"', 34))
        self.assertEqual(ascii_value('a' * 1000), 97)
        self.assertEqual(ascii_value('a' * 10000), 97)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ascii_value(None)
        with self.assertRaises(TypeError):
            ascii_value(123)
        with self.assertRaises(TypeError):
            ascii_value([1, 2, 3])
        with self.assertRaises(TypeError):
            ascii_value({'a': 1, 'b': 2})
