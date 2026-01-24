import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(replace_blank("Hello World", "*"), "Hello*World")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_blank("", "*"), "")

    def test_edge_case_single_char_string(self):
        self.assertEqual(replace_blank("a", "*"), "a")

    def test_edge_case_single_space_string(self):
        self.assertEqual(replace_blank(" ", "*"), "*")

    def test_edge_case_multiple_spaces_string(self):
        self.assertEqual(replace_blank("   ", "*"), "***")

    def test_edge_case_multiple_chars_string(self):
        self.assertEqual(replace_blank("Hello World", "++"), "Hello++World")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            replace_blank(123, "*")

    def test_edge_case_non_string_char(self):
        with self.assertRaises(TypeError):
            replace_blank("Hello World", 123)
