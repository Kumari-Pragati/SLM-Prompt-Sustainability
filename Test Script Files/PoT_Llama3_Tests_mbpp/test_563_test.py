import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_values('"hello" "world"'), ['"hello"', '"world"'])

    def test_edge_case_empty_string(self):
        self.assertEqual(extract_values(""), [])

    def test_edge_case_single_quote(self):
        self.assertEqual(extract_values('"hello"'), ['"hello"'])

    def test_edge_case_no_quotes(self):
        self.assertEqual(extract_values("hello world"), [])

    def test_edge_case_multiple_quotes(self):
        self.assertEqual(extract_values('"hello" "world" "python"'), ['"hello"', '"world"', '"python"'])

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            extract_values(123)

    def test_edge_case_non_string_input_list(self):
        with self.assertRaises(TypeError):
            extract_values(["hello", "world"])

    def test_edge_case_non_string_input_dict(self):
        with self.assertRaises(TypeError):
            extract_values({"hello": "world"})
