import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(toggle_string("Hello, World!"), "hELLO, wRLD!")

    def test_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_single_letter(self):
        self.assertEqual(toggle_string("a"), "A")
        self.assertEqual(toggle_string("z"), "Z")

    def test_all_uppercase(self):
        self.assertEqual(toggle_string("HELLO"), "hello")

    def test_all_lowercase(self):
        self.assertEqual(toggle_string("hello"), "HELLO")

    def test_special_characters(self):
        self.assertEqual(toggle_string("!Hello, World$"), "!hELLO, wRLD$")

    def test_invalid_input(self):
        self.assertRaises(TypeError, toggle_string, 123)
        self.assertRaises(TypeError, toggle_string, None)
        self.assertRaises(TypeError, toggle_string, [])
