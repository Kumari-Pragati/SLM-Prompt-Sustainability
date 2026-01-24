import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(extract_quotation('This is a "test" example.'), ['"test"'])

    def test_multiple_quotes(self):
        self.assertListEqual(extract_quotation('This is a "test" example with "multiple" quotes.'), ['"test"', '"multiple"'])

    def test_empty_string(self):
        self.assertListEqual(extract_quotation(''), [])

    def test_no_quotes(self):
        self.assertListEqual(extract_quotation('This is an example.'), [])

    def test_leading_trailing_whitespace(self):
        self.assertListEqual(extract_quotation('   "test"   '), ['"test"'])

    def test_escaped_quotes(self):
        self.assertListEqual(extract_quotation('This is a "test" example with \\"escaped\\" quotes.'), ['"test"', '\\"escaped\\""'])

    def test_quotes_in_numbers(self):
        self.assertListEqual(extract_quotation('This is a "123" test example.'), ['"123"'])

    def test_quotes_in_symbols(self):
        self.assertListEqual(extract_quotation('This is a "1+1=2" test example.'), ['"1+1=2"'])
