import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):
    def test_typical_use_case(self):
        text = "Hello, World! 123"
        expected_output = "Hello World 123"
        self.assertEqual(remove_splchar(text), expected_output)

    def test_edge_case_empty_string(self):
        text = ""
        expected_output = ""
        self.assertEqual(remove_splchar(text), expected_output)

    def test_edge_case_single_char(self):
        text = "a"
        expected_output = "a"
        self.assertEqual(remove_splchar(text), expected_output)

    def test_edge_case_multiple_chars(self):
        text = "abc def"
        expected_output = "abcdef"
        self.assertEqual(remove_splchar(text), expected_output)

    def test_edge_case_non_ascii_chars(self):
        text = "Hello, World! 123"
        expected_output = "Hello World 123"
        self.assertEqual(remove_splchar(text), expected_output)

    def test_invalid_input_non_string(self):
        text = 123
        with self.assertRaises(TypeError):
            remove_splchar(text)
