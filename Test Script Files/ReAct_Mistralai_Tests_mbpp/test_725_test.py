import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual([], extract_quotation(""))

    def test_single_quotation(self):
        self.assertListEqual(["'single quote'"], extract_quotation("'single quote'"))

    def test_multiple_quotations(self):
        self.assertListEqual(["'first quote'", "'second quote'", "'third quote'"],
                              extract_quotation("'first quote' 'second quote' 'third quote'"))

    def test_escaped_quotation(self):
        self.assertListEqual(["'single quote'", "\\'escaped quote\\'"],
                              extract_quotation("'single quote' \\'escaped quote\\'"))

    def test_no_opening_quotation(self):
        self.assertListEqual([], extract_quotation("'second quote'"))

    def test_no_closing_quotation(self):
        self.assertListEqual([], extract_quotation("'first quote"))

    def test_mixed_quotes(self):
        self.assertListEqual(["'single quote'", '"double quote"'], extract_quotation("'single quote' 'double quote'"))

    def test_trailing_whitespace(self):
        self.assertListEqual(["'single quote'", "   'double quote with trailing whitespace   '"],
                              extract_quotation("'single quote' 'double quote with trailing whitespace   '"))

    def test_leading_whitespace(self):
        self.assertListEqual(["'single quote with leading whitespace'", "'double quote'"],
                              extract_quotation("'single quote with leading whitespace' 'double quote'"))

    def test_multiple_escaped_quotations(self):
        self.assertListEqual(["'single quote'", "\\'escaped quote\\'", "\\\\'double backslash\\'"],
                              extract_quotation("'single quote' \\'escaped quote\\' \\\\'double backslash\\'"))
