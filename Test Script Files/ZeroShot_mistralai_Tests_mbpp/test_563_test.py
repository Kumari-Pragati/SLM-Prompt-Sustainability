import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(extract_values(''), [])

    def test_single_value(self):
        self.assertListEqual(extract_values('"value"'), ['value'])

    def test_multiple_values(self):
        self.assertListEqual(extract_values('"value1" "value2" "value3"'), ['value1', 'value2', 'value3'])

    def test_values_with_spaces(self):
        self.assertListEqual(extract_values('"value 1" "value 2" "value 3"'), ['value 1', 'value 2', 'value 3'])

    def test_values_with_special_characters(self):
        self.assertListEqual(extract_values('"value1, comma" "value2. dot" "value3!@#"'), ['value1, comma', 'value2. dot', 'value3!@#'])

    def test_values_with_escaped_quotes(self):
        self.assertListEqual(extract_values('"value1\\"" "value2\\"" "value3\\""'), ['value1"', 'value2"', 'value3"'])

    def test_values_with_nested_quotes(self):
        self.assertListEqual(extract_values('"value1""value2""value3"'), ['value1"value2"value3'])
