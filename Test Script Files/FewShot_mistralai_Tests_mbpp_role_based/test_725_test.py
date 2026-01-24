import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(extract_quotation(''), [])

    def test_single_quotation(self):
        self.assertListEqual(extract_quotation('"Hello World"'), ['Hello World'])

    def test_multiple_quotations(self):
        self.assertListEqual(extract_quotation('"Hello World" "Goodbye World"'), ['Hello World', 'Goodbye World'])

    def test_escaped_quotation(self):
        self.assertListEqual(extract_quotation('"Hello World" with escaped quotation "\\"' ), ['Hello World', '\\'])

    def test_trailing_and_leading_whitespace(self):
        self.assertListEqual(extract_quotation('   "Hello World"   '), ['Hello World'])

    def test_no_quotation(self):
        self.assertListEqual(extract_quotation('Hello World'), [])

    def test_invalid_input(self):
        self.assertRaises(ValueError, extract_quotation, 'invalid input')
