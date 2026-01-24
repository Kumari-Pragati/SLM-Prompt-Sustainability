import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(extract_quotation(""), [])

    def test_single_quotation(self):
        self.assertListEqual(extract_quotation("'Hello World'"), ["Hello World"])

    def test_multiple_quotations(self):
        self.assertListEqual(extract_quotation("'Hello World', 'Nice to meet you'"), ["Hello World", "Nice to meet you"])

    def test_escaped_quotation(self):
        self.assertListEqual(extract_quotation("'It's a 'great' day'"), ["It's a 'great' day"])

    def test_quotation_at_start_and_end(self):
        self.assertListEqual(extract_quotation("'Hello World'" ), ["Hello World"])

    def test_quotation_in_middle(self):
        self.assertListEqual(extract_quotation("'Hello World, Nice to meet you'"), ["World, Nice to meet you"])

    def test_multiple_escaped_quotations(self):
        self.assertListEqual(extract_quotation("'It''s a ''great'' day''"), ["It's a 'great' day"])

    def test_no_quotations(self):
        self.assertListEqual(extract_quotation("Hello World"), [])

    def test_whitespace_around_quotation(self):
        self.assertListEqual(extract_quotation("   'Hello World'   "), ["Hello World"])

    def test_invalid_input(self):
        self.assertRaises(TypeError, extract_quotation, 123)
