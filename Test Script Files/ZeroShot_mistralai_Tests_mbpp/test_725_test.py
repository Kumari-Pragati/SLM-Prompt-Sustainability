import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(extract_quotation(""), [])

    def test_single_quotation(self):
        self.assertListEqual(extract_quotation("'Hello, World!'"), ["Hello, World!"])

    def test_multiple_quotations(self):
        self.assertListEqual(extract_quotation('"Hello", "World", "!"'), ["Hello", "World", "!"])

    def test_nested_quotations(self):
        self.assertListEqual(extract_quotation('"Hello" "World" "!"'), ["Hello", "World", "!"])

    def test_mixed_quotations(self):
        self.assertListEqual(extract_quotation("'Hello', 'World', '!'"), ["Hello", "World", "!"])

    def test_escaped_quotations(self):
        self.assertListEqual(extract_quotation("'Hello\\' World\\!'"), ["Hello'", "World", "!"])

    def test_trailing_and_leading_whitespace(self):
        self.assertListEqual(extract_quotation("   'Hello, World!'   "), ["Hello, World!"])

    def test_multiple_whitespace_between_quotations(self):
        self.assertListEqual(extract_quotation("'Hello'   'World'   '!'"), ["Hello", "World", "!"])
