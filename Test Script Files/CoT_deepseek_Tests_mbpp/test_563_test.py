import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_typical_case(self):
        text = 'Some text with "value1" and "value2"'
        self.assertEqual(extract_values(text), ['value1', 'value2'])

    def test_single_value(self):
        text = 'Single value "single"'
        self.assertEqual(extract_values(text), ['single'])

    def test_no_values(self):
        text = 'Text without any quotes'
        self.assertEqual(extract_values(text), [])

    def test_empty_string(self):
        text = ''
        self.assertEqual(extract_values(text), [])

    def test_nested_values(self):
        text = 'Nested values "value1" and "value2" and "value3"'
        self.assertEqual(extract_values(text), ['value1', 'value2', 'value3'])

    def test_escaped_quotes(self):
        text = 'Text with escaped quotes "value \\"escaped\\""'
        self.assertEqual(extract_values(text), ['value "escaped"'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_values(123)
