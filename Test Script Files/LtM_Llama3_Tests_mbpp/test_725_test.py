import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(extract_quotation('"hello"'), ['"hello"'])
        self.assertEqual(extract_quotation('"hello world"'), ['"hello world"'])
        self.assertEqual(extract_quotation('"'), [])

    def test_edge(self):
        self.assertEqual(extract_quotation(''), [])
        self.assertEqual(extract_quotation('"'), [])
        self.assertEqual(extract_quotation('"hello" "world"'), ['"hello"', '"world"'])

    def test_complex(self):
        self.assertEqual(extract_quotation('"hello" "world" "python"'), ['"hello"', '"world"', '"python"'])
        self.assertEqual(extract_quotation('"hello" "world" "python" "unittest"'), ['"hello"', '"world"', '"python"', '"unittest"'])
