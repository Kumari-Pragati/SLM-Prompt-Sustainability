import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(first_repeated_char("abc"), 'a')
        self.assertEqual(first_repeated_char("aab"), 'a')
        self.assertEqual(first_repeated_char("abcde"), 'a')

    def test_edge_cases(self):
        self.assertEqual(first_repeated_char(""), "None")
        self.assertEqual(first_repeated_char("a"), 'a')
        self.assertEqual(first_repeated_char("aabb"), 'a')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_repeated_char(123)
        with self.assertRaises(TypeError):
            first_repeated_char(None)

    def test_complex_inputs(self):
        self.assertEqual(first_repeated_char("abab"), 'a')
        self.assertEqual(first_repeated_char("abcabc"), 'a')
        self.assertEqual(first_repeated_char("abcdef"), "None")
