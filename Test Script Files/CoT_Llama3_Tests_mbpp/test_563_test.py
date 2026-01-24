import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_typical_input(self):
        text = '"hello" "world" "python"'
        self.assertEqual(extract_values(text), ['hello', 'world', 'python'])

    def test_edge_case_empty_string(self):
        text = ''
        self.assertEqual(extract_values(text), [])

    def test_edge_case_single_quote(self):
        text = '"hello"'
        self.assertEqual(extract_values(text), ['hello'])

    def test_edge_case_multiple_quotes(self):
        text = '"hello" "world" "python" "again"'
        self.assertEqual(extract_values(text), ['hello', 'world', 'python', 'again'])

    def test_edge_case_no_quotes(self):
        text = 'hello world python'
        self.assertEqual(extract_values(text), [])

    def test_invalid_input_non_string(self):
        text = 123
        with self.assertRaises(TypeError):
            extract_values(text)

    def test_invalid_input_non_string_list(self):
        text = [1, 2, 3]
        with self.assertRaises(TypeError):
            extract_values(text)
