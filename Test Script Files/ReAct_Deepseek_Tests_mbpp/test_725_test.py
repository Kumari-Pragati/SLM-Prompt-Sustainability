import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_typical_case(self):
        text = 'He said, "Hello, world!"'
        self.assertEqual(extract_quotation(text), ['Hello, world!'])

    def test_no_quotation(self):
        text = 'He said, world!'
        self.assertEqual(extract_quotation(text), [])

    def test_multiple_quotations(self):
        text = 'He said, "Hello, world!" and she said, "Goodbye, world!"'
        self.assertEqual(extract_quotation(text), ['Hello, world!', 'Goodbye, world!'])

    def test_empty_string(self):
        text = ''
        self.assertEqual(extract_quotation(text), [])

    def test_single_quote_instead_of_double(self):
        text = "He said, 'Hello, world!'"
        self.assertEqual(extract_quotation(text), [])

    def test_nested_quotations(self):
        text = 'He said, "She said, "Hello, world!""'
        self.assertEqual(extract_quotation(text), ['She said, "Hello, world!"'])

    def test_escaped_quotation_marks(self):
        text = 'He said, "She said, \\"Hello, world!\\""'
        self.assertEqual(extract_quotation(text), ['She said, "Hello, world!"'])
