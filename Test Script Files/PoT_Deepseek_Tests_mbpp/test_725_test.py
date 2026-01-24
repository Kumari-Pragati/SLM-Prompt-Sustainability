import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_typical_case(self):
        text = 'He said, "Hello, world!"'
        self.assertEqual(extract_quotation(text), ['Hello, world!'])

    def test_edge_case_no_quotes(self):
        text = 'Hello, world!'
        self.assertEqual(extract_quotation(text), [])

    def test_boundary_case_empty_string(self):
        text = ''
        self.assertEqual(extract_quotation(text), [])

    def test_corner_case_multiple_quotes(self):
        text = 'He said, "Hello, world!" and she said, "Goodbye, world!"'
        self.assertEqual(extract_quotation(text), ['Hello, world!', 'Goodbye, world!'])

    def test_corner_case_nested_quotes(self):
        text = 'He said, "She said, "Hello, world!""'
        self.assertEqual(extract_quotation(text), ['She said, "Hello, world!"'])
