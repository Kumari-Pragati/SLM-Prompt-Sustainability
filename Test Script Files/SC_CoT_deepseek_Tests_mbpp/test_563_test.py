import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_typical_case(self):
        text = 'Some text with "quoted text" and another "quoted text" in it.'
        expected_output = ['quoted text', 'quoted text']
        self.assertEqual(extract_values(text), expected_output)

    def test_single_quote(self):
        text = 'Some text with "quoted text" and another "quoted text" in it.'
        expected_output = ['quoted text', 'quoted text']
        self.assertEqual(extract_values(text), expected_output)

    def test_no_quotes(self):
        text = 'Some text with quoted text and another quoted text in it.'
        expected_output = []
        self.assertEqual(extract_values(text), expected_output)

    def test_empty_string(self):
        text = ''
        expected_output = []
        self.assertEqual(extract_values(text), expected_output)

    def test_nested_quotes(self):
        text = 'Nested quotes: "He said, "Hello, World!""'
        expected_output = ['He said, "Hello, World!"']
        self.assertEqual(extract_values(text), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_values(123)
