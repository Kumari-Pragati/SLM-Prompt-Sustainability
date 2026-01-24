import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(extract_values('"value1" "value2" "value3"'), ['value1', 'value2', 'value3'])

    def test_empty_input(self):
        self.assertListEqual(extract_values(''), [])

    def test_single_input(self):
        self.assertListEqual(extract_values('"value"'), ['value'])

    def test_leading_trailing_spaces(self):
        self.assertListEqual(extract_values('   "value"   '), ['value'])

    def test_escaped_quotes(self):
        self.assertListEqual(extract_values('"value with \"escaped\" quotes"'), ['value with "escaped" quotes'])

    def test_empty_quotes(self):
        self.assertListEqual(extract_values('""'), [])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            extract_values('"value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value" "value