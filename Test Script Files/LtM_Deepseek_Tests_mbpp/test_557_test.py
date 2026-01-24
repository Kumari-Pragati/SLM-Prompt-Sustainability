import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_toggle_simple_string(self):
        self.assertEqual(toggle_string("Hello"), "hELLO")

    def test_toggle_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_toggle_string_with_numbers_and_symbols(self):
        self.assertEqual(toggle_string("HeLlo123!"), "hEllO123!")

    def test_toggle_string_with_special_characters(self):
        self.assertEqual(toggle_string("!@#$%^&*()"), "!@#$%^&*()")

    def test_toggle_string_with_mixed_case(self):
        self.assertEqual(toggle_string("hEllO"), "Hello")
