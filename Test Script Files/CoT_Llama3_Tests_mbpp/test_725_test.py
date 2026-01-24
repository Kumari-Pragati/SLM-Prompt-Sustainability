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

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_quotation(123)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            extract_quotation([1, 2, 3])
