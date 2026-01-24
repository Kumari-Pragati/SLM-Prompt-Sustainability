import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_extract_single_value(self):
        self.assertEqual(extract_values('"value"'), ['value'])

    def test_extract_multiple_values(self):
        self.assertEqual(extract_values('"value1" "value2" "value3"'), ['value1', 'value2', 'value3'])

    def test_empty_string(self):
        self.assertEqual(extract_values(''), [])

    def test_no_quotes(self):
        self.assertEqual(extract_values('value'), [])

    def test_escaped_quotes(self):
        self.assertEqual(extract_values('"value with \"escaped\" quotes"'), ['value with "escaped" quotes'])

    def test_quotes_in_values(self):
        self.assertEqual(extract_values('"value with "inner" quotes"'), ['value with "inner" quotes'])

    def test_trailing_and_leading_whitespace(self):
        self.assertEqual(extract_values('   "value with leading and trailing whitespace"   '), ['value with leading and trailing whitespace'])
