import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_single_quotation(self):
        self.assertEqual(extract_quotation('"Hello, World!'), ['Hello, World!'])

    def test_multiple_quotations(self):
        self.assertEqual(extract_quotation('"Hello, World!" "How are you?"'), ['Hello, World!', 'How are you?'])

    def test_no_quotation(self):
        self.assertEqual(extract_quotation('Hello, World! How are you?'), [])

    def test_empty_string(self):
        self.assertEqual(extract_quotation(''), [])

    def test_nested_quotations(self):
        self.assertEqual(extract_quotation('"Hello, "World"'), ['Hello, "World"'])
