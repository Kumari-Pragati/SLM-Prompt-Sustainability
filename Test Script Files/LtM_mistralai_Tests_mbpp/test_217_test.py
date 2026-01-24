import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_simple_single_char(self):
        self.assertEqual(first_Repeated_Char('a'), 'a')

    def test_simple_multiple_chars(self):
        self.assertEqual(first_Repeated_Char('abc'), '\0')
        self.assertEqual(first_Repeated_Char('abca'), 'a')

    def test_edge_case_single_char_repeat(self):
        self.assertEqual(first_Repeated_Char('aa'), 'a')

    def test_edge_case_multiple_chars_repeat(self):
        self.assertEqual(first_Repeated_Char('aaaa'), 'a')
        self.assertEqual(first_Repeated_Char('abab'), '\0')

    def test_boundary_case_empty_string(self):
        self.assertEqual(first_Repeated_Char(''), '\0')

    def test_boundary_case_single_digit(self):
        self.assertEqual(first_Repeated_Char('1'), '\0')

    def test_boundary_case_special_char(self):
        self.assertEqual(first_Repeated_Char('!@#$%^&*()'), '\0')
