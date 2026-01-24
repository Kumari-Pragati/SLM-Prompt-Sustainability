import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(extract_values(''), [])

    def test_single_value(self):
        self.assertListEqual(extract_values('"Test"'), ['Test'])

    def test_multiple_values(self):
        self.assertListEqual(extract_values('"Test1" "Test2" "Test3"'), ['Test1', 'Test2', 'Test3'])

    def test_values_with_spaces(self):
        self.assertListEqual(extract_values('"Test 1" "Test 2"'), ['Test 1', 'Test 2'])

    def test_values_with_special_characters(self):
        self.assertListEqual(extract_values('"Test1$" "Test2_"'), ['Test1$', 'Test2_'])

    def test_values_with_newlines(self):
        self.assertListEqual(extract_values('"\nTest1\n" "Test2"'), ['Test1', 'Test2'])

    def test_values_with_escaped_quotes(self):
        self.assertListEqual(extract_values('"\"Test\""'), ['"Test"'])

    def test_values_with_empty_string(self):
        self.assertListEqual(extract_values('"Test" "" "Test"'), ['Test', '', 'Test'])

    def test_values_with_non_string(self):
        with self.assertRaises(TypeError):
            extract_values(123)

    def test_values_with_non_quoted_string(self):
        with self.assertRaises(ValueError):
            extract_values('Test Test')
