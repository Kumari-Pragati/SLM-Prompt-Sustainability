import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_char_position('ABC'), 3)
        self.assertEqual(count_char_position('abc'), 3)
        self.assertEqual(count_char_position('Abc'), 3)
        self.assertEqual(count_char_position('AbCdEfGhI'), 5)

    def test_edge_cases(self):
        self.assertEqual(count_char_position(''), 0)
        self.assertEqual(count_char_position('123'), 0)
        self.assertEqual(count_char_position('!@#'), 0)
        self.assertEqual(count_char_position('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 52)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            count_char_position(123)
        with self.assertRaises(TypeError):
            count_char_position(['A', 'B', 'C'])
