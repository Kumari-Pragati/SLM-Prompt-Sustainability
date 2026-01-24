import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(first_Repeated_Char("abcde"), 'b')
        self.assertEqual(first_Repeated_Char("aabbcc"), 'a')
        self.assertEqual(first_Repeated_Char("hello"), 'l')

    def test_edge_cases(self):
        self.assertEqual(first_Repeated_Char(""), '\0')
        self.assertEqual(first_Repeated_Char("a"), 'a')
        self.assertEqual(first_Repeated_Char("abcdef"), 'a')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_Repeated_Char(123)
        with self.assertRaises(TypeError):
            first_Repeated_Char(None)

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            first_Repeated_Char([1, 2, 3])
