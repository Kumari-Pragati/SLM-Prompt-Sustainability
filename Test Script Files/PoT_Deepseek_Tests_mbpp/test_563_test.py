import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_typical_case(self):
        text = 'Some "typical" text with "multiple" values'
        expected_output = ['typical', 'multiple']
        self.assertEqual(extract_values(text), expected_output)

    def test_empty_string(self):
        text = ''
        expected_output = []
        self.assertEqual(extract_values(text), expected_output)

    def test_no_quotes(self):
        text = 'No quotes here'
        expected_output = []
        self.assertEqual(extract_values(text), expected_output)

    def test_single_quote(self):
        text = 'Single quote: "value"'
        expected_output = ['value']
        self.assertEqual(extract_values(text), expected_output)

    def test_multiple_spaces(self):
        text = 'Multiple   spaces "around" values'
        expected_output = ['around']
        self.assertEqual(extract_values(text), expected_output)

    def test_nested_quotes(self):
        text = 'Nested quotes: "He said, "Hello, World!""'
        expected_output = ['He said, "Hello, World!"']
        self.assertEqual(extract_values(text), expected_output)

    def test_no_matching_quotes(self):
        text = 'No matching quotes "
        expected_output = []
        self.assertEqual(extract_values(text), expected_output)
