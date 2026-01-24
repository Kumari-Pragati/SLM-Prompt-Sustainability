import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_typical_case(self):
        text1 = 'He said, "Hello, world!"'
        expected_output = ['Hello, world!']
        self.assertEqual(extract_quotation(text1), expected_output)

    def test_no_quotation(self):
        text1 = 'He said, Hello, world!'
        expected_output = []
        self.assertEqual(extract_quotation(text1), expected_output)

    def test_multiple_quotations(self):
        text1 = 'He said, "Hello, world!" and she said, "Goodbye, world!"'
        expected_output = ['Hello, world!', 'Goodbye, world!']
        self.assertEqual(extract_quotation(text1), expected_output)

    def test_empty_string(self):
        text1 = ''
        expected_output = []
        self.assertEqual(extract_quotation(text1), expected_output)

    def test_nested_quotations(self):
        text1 = 'He said, "She said, "Hello, world!""'
        expected_output = ['She said, "Hello, world!"']
        self.assertEqual(extract_quotation(text1), expected_output)

    def test_special_characters_in_quotation(self):
        text1 = 'He said, "Hello, world! :)"'
        expected_output = ['Hello, world! :)']
        self.assertEqual(extract_quotation(text1), expected_output)
