import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(extract_values(""), [])

    def test_single_value(self):
        self.assertListEqual(extract_values('"test"'), ['test'])

    def test_multiple_values(self):
        self.assertListEqual(extract_values('"test1" "test2" "test3"'), ['test1', 'test2', 'test3'])

    def test_values_with_spaces(self):
        self.assertListEqual(extract_values('"test1" "test 2" "test 3"'), ['test1', 'test 2', 'test 3'])

    def test_values_with_special_characters(self):
        self.assertListEqual(extract_values('"test1$" "test2#" "test3@"'), ['test1$', 'test2#', 'test3@'])

    def test_values_with_newlines(self):
        self.assertListEqual(extract_values('"\ntest1\n" "test2\n" "test3\n"'), ['test1', 'test2', 'test3'])

    def test_values_with_escaped_quotes(self):
        self.assertListEqual(extract_values('"test1\" "test2\\"" "test3\\\\"'), ['test1"', 'test2""', 'test3\\'])

    def test_values_with_empty_string(self):
        self.assertListEqual(extract_values('"test1" "" "test3"'), ['test1', '', 'test3'])

    def test_values_with_nested_quotes(self):
        self.assertListEqual(extract_values('"test1""test2" "test3"'), ['test1""test2', 'test3'])

    def test_values_with_escaped_backslashes(self):
        self.assertListEqual(extract_values('"test1\\\\\\\\" "test2\\\\\\\\\\"'), ['test1\\\\\\', 'test2\\\\\\\\'])
