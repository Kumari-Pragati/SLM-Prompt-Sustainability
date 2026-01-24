import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_repeated_char('abcab'), 'a')
        self.assertEqual(first_repeated_char('hello'), 'l')
        self.assertEqual(first_repeated_char('123123'), '1')

    def test_edge_cases(self):
        self.assertEqual(first_repeated_char(''), 'None')
        self.assertEqual(first_repeated_char('a'), 'None')
        self.assertEqual(first_repeated_char('abcd'), 'None')

    def test_corner_cases(self):
        self.assertEqual(first_repeated_char('aabbcc'), 'a')
        self.assertEqual(first_repeated_char('abcabc'), 'a')
        self.assertEqual(first_repeated_char('123123123'), '1')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_repeated_char(123)
        with self.assertRaises(TypeError):
            first_repeated_char(None)
        with self.assertRaises(TypeError):
            first_repeated_char(['a', 'b', 'c'])
