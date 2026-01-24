import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO WORLD")

    def test_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_single_letter(self):
        self.assertEqual(toggle_string("a"), "A")
        self.assertEqual(toggle_string("z"), "Z")

    def test_uppercase_string(self):
        self.assertEqual(toggle_string("HELLO"), "hello")

    def test_mixed_case_string(self):
        self.assertEqual(toggle_string("HeLlO wOrLd"), "heLLo wOrLD")

    def test_special_characters(self):
        self.assertEqual(toggle_string("Hello@123_World"), "hELLO@123_WORLD")

    def test_error_case(self):
        with self.assertRaises(TypeError):
            toggle_string(123)
