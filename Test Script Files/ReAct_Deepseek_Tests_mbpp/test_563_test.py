import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_typical_case(self):
        text = 'Some text with "value1" and another "value2"'
        expected_result = ['value1', 'value2']
        self.assertEqual(extract_values(text), expected_result)

    def test_no_values(self):
        text = 'Some text without any quotes'
        expected_result = []
        self.assertEqual(extract_values(text), expected_result)

    def test_empty_string(self):
        text = ''
        expected_result = []
        self.assertEqual(extract_values(text), expected_result)

    def test_single_quote(self):
        text = 'Text with single quote: \'value\''
        expected_result = ['value']
        self.assertEqual(extract_values(text), expected_result)

    def test_nested_quotes(self):
        text = 'Nested quotes: "He said, "Hello, World!""'
        expected_result = ['He said, "Hello, World!"']
        self.assertEqual(extract_values(text), expected_result)

    def test_special_characters_in_quotes(self):
        text = 'Text with special characters: "value!@#"'
        expected_result = ['value!@#']
        self.assertEqual(extract_values(text), expected_result)

    def test_multiple_spaces_in_quotes(self):
        text = 'Text with multiple spaces: "value   with   spaces"'
        expected_result = ['value   with   spaces']
        self.assertEqual(extract_values(text), expected_result)
