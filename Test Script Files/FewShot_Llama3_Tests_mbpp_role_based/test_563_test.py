import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_valid_input(self):
        text = '"Hello", "World", "Python"'
        expected_output = ['"Hello"', '"World"', '"Python"']
        self.assertEqual(extract_values(text), expected_output)

    def test_empty_input(self):
        text = ''
        expected_output = []
        self.assertEqual(extract_values(text), expected_output)

    def test_no_matches(self):
        text = 'This is a test sentence without quotes.'
        expected_output = []
        self.assertEqual(extract_values(text), expected_output)

    def test_multiple_matches(self):
        text = '"Hello", "World", "Python", "Extract", "Values"'
        expected_output = ['"Hello"', '"World"', '"Python"', '"Extract"', '"Values"']
        self.assertEqual(extract_values(text), expected_output)
