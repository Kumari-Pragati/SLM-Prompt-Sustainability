import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_quotation('"Hello, world!"'), ['"Hello, world!"'])

    def test_multiple_quotations(self):
        self.assertEqual(extract_quotation('"Hello, world!" "Python is fun!"'), ['"Hello, world!"', '"Python is fun!"]')

    def test_empty_string(self):
        self.assertEqual(extract_quotation(""), [])

    def test_no_quotations(self):
        self.assertEqual(extract_quotation("This is a test"), [])

    def test_quotation_with_newline(self):
        self.assertEqual(extract_quotation('"Hello,\nworld!"'), ['"Hello,\nworld!"'])

    def test_quotation_with_escape_characters(self):
        self.assertEqual(extract_quotation('"Hello, world!\"'), ['"Hello, world!\"'])
