import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):
    def test_typical_use_case(self):
        text1 = 'He said, "Hello, world!"'
        self.assertEqual(extract_quotation(text1), ['Hello, world!'])

    def test_edge_case_no_quotation(self):
        text1 = 'He said, Hello, world!'
        self.assertEqual(extract_quotation(text1), [])

    def test_boundary_case_empty_string(self):
        text1 = ''
        self.assertEqual(extract_quotation(text1), [])

    def test_boundary_case_single_quotation(self):
        text1 = '"Hello, world!"'
        self.assertEqual(extract_quotation(text1), ['Hello, world!'])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_quotation(123)
