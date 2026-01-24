import unittest
from mbpp_396_code import check_char

class TestCheckChar(unittest.TestCase):

    def test_valid_chars(self):
        self.assertEqual(check_char('a'), "Valid")
        self.assertEqual(check_char('z'), "Valid")
        self.assertEqual(check_char('b'), "Valid")
        self.assertEqual(check_char('aa'), "Valid")
        self.assertEqual(check_char('aaa'), "Valid")
        self.assertEqual(check_char('abcba'), "Valid")

    def test_invalid_chars(self):
        self.assertEqual(check_char(''), "Invalid")
        self.assertEqual(check_char('A'), "Invalid")
        self.assertEqual(check_char('1'), "Invalid")
        self.assertEqual(check_char(' '), "Invalid")
        self.assertEqual(check_char('ab'), "Invalid")
        self.assertEqual(check_char('abcabc'), "Invalid")
