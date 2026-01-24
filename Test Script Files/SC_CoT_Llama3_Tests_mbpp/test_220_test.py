import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 2), "Hello:world!")

    def test_edge_case_n_zero(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 0), "Hello, world!")

    def test_edge_case_n_max(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 10), "Hello:world!")

    def test_edge_case_n_min(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", -1), "Hello, world!")

    def test_edge_case_text_empty(self):
        self.assertEqual(replace_max_specialchar("", 2), "")

    def test_edge_case_text_single_char(self):
        self.assertEqual(replace_max_specialchar("a", 2), "a")

    def test_edge_case_text_single_space(self):
        self.assertEqual(replace_max_specialchar(" ", 2), " ")

    def test_edge_case_text_single_comma(self):
        self.assertEqual(replace_max_specialchar(",", 2), ",")

    def test_edge_case_text_single_dot(self):
        self.assertEqual(replace_max_specialchar(".", 2), ".")

    def test_edge_case_text_multiple_spaces(self):
        self.assertEqual(replace_max_specialchar("   ", 2), "   ")

    def test_edge_case_text_multiple_commas(self):
        self.assertEqual(replace_max_specialchar(",,,,", 2), "::::")

    def test_edge_case_text_multiple_dots(self):
        self.assertEqual(replace_max_specialchar("...,,", 2), "::::")

    def test_edge_case_text_multiple_chars(self):
        self.assertEqual(replace_max_specialchar("hello, world!", 2), "hello:world!")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar("hello, world!", "a")

    def test_invalid_input_negative_integer(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar("hello, world!", -1)
