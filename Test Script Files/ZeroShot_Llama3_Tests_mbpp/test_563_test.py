import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_extract_values(self):
        text = '"hello" "world" "python"'
        self.assertEqual(extract_values(text), ['"hello"', '"world"', '"python"'])

    def test_extract_values_multiple_lines(self):
        text = '"hello" "world"\n"python" "unittest"'
        self.assertEqual(extract_values(text), ['"hello"', '"world"', '"python"', '"unittest"'])

    def test_extract_values_empty_string(self):
        text = ''
        self.assertEqual(extract_values(text), [])

    def test_extract_values_no_quotes(self):
        text = 'hello world python'
        self.assertEqual(extract_values(text), [])

    def test_extract_values_no_matches(self):
        text = 'This is a test sentence without quotes.'
        self.assertEqual(extract_values(text), [])
