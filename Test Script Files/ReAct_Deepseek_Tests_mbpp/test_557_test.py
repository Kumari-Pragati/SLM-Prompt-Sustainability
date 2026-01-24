import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_toggle_string_typical(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")
        self.assertEqual(toggle_string("Python is FUN"), "pYTHON IS fun")

    def test_toggle_string_empty(self):
        self.assertEqual(toggle_string(""), "")

    def test_toggle_string_single_char(self):
        self.assertEqual(toggle_string("a"), "A")
        self.assertEqual(toggle_string("A"), "a")

    def test_toggle_string_special_chars(self):
        self.assertEqual(toggle_string("!@#$%^&*()"), "!@#$%^&*()")

    def test_toggle_string_numbers(self):
        self.assertEqual(toggle_string("1234567890"), "1234567890")
