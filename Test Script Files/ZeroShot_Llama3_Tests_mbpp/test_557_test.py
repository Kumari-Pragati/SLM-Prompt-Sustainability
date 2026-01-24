import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_toggle_string(self):
        self.assertEqual(toggle_string("Hello"), "hELLO")
        self.assertEqual(toggle_string("WORLD"), "wORLD")
        self.assertEqual(toggle_string("Python"), "pYTHON")
        self.assertEqual(toggle_string("123"), "123")
        self.assertEqual(toggle_string("abc"), "abc")
        self.assertEqual(toggle_string("ABC123"), "AbC123")
        self.assertEqual(toggle_string("hello world"), "HELLO WORLD")
        self.assertEqual(toggle_string("Python is awesome"), "pYTHON IS AWESOME")
