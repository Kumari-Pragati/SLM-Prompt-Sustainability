import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_repeated_char('abcab'), 'a')
        self.assertEqual(first_repeated_char('abcabc'), 'a')
        self.assertEqual(first_repeated_char('abcd'), 'None')

    def test_edge_cases(self):
        self.assertEqual(first_repeated_char(''), 'None')
        self.assertEqual(first_repeated_char('a'), 'None')
        self.assertEqual(first_repeated_char('aa'), 'a')
        self.assertEqual(first_repeated_char('aaa'), 'a')

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            first_repeated_char(123)
        with self.assertRaises(TypeError):
            first_repeated_char(['a', 'b', 'c'])
