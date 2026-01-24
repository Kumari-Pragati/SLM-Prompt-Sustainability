import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):
    def test_typical_use_case(self):
        text = '"Hello, world!" "This is a test." "Another quote."'
        self.assertEqual(extract_quotation(text), ["Hello, world!", "This is a test.", "Another quote."])

    def test_empty_string(self):
        text = ''
        self.assertEqual(extract_quotation(text), [])

    def test_no_quotations(self):
        text = 'This is a test without any quotations.'
        self.assertEqual(extract_quotation(text), [])

    def test_multiple_quotations(self):
        text = '"Hello, world!" "This is a test." "Another quote." "Yet another one."'
        self.assertEqual(extract_quotation(text), ["Hello, world!", "This is a test.", "Another quote.", "Yet another one."])

    def test_quotations_with_newlines(self):
        text = '"Hello, world!\nThis is a test." "Another quote."'
        self.assertEqual(extract_quotation(text), ["Hello, world!\nThis is a test.", "Another quote."])
