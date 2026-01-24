import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")

    def test_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_single_character(self):
        self.assertEqual(toggle_string("a"), "A")

    def test_all_uppercase(self):
        self.assertEqual(toggle_string("HELLO"), "HELLO")

    def test_all_lowercase(self):
        self.assertEqual(toggle_string("hello"), "hello")

    def test_mixed_case(self):
        self.assertEqual(toggle_string("HeLlO"), "HeLlO")
