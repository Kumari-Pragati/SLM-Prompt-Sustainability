import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_typical_case(self):
        text = '"hello" "world" "python"'
        self.assertEqual(extract_values(text), ["hello", "world", "python"])

    def test_edge_case_empty_string(self):
        text = ''
        self.assertEqual(extract_values(text), [])

    def test_edge_case_no_quotes(self):
        text = 'hello world python'
        self.assertEqual(extract_values(text), [])

    def test_edge_case_no_matches(self):
        text = 'This is a test string with no matches'
        self.assertEqual(extract_values(text), [])

    def test_edge_case_multiple_matches(self):
        text = '"hello" "world" "python" "react" "unittest"'
        self.assertEqual(extract_values(text), ["hello", "world", "python", "react", "unittest"])

    def test_edge_case_invalid_input(self):
        text = 123
        with self.assertRaises(TypeError):
            extract_values(text)
