import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(extract_quotation('"Hello, world!"'), ['Hello, world!'])

    def test_edge_condition_empty_input(self):
        self.assertEqual(extract_quotation(''), [])

    def test_edge_condition_no_quotes(self):
        self.assertEqual(extract_quotation('Hello, world!'), [])

    def test_boundary_condition_single_quote(self):
        self.assertEqual(extract_quotation("It's a beautiful day"), ['It\'s a beautiful day'])

    def test_complex_input_multiple_quotes(self):
        self.assertEqual(extract_quotation('He said, "Hello, world!" and she said, "Goodbye, world!"'), 
                         ['Hello, world!', 'Goodbye, world!'])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_quotation(123)
