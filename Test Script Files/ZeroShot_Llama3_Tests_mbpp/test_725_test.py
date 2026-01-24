import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_extract_quotation(self):
        self.assertEqual(extract_quotation('"Hello, world!"'), ['"Hello, world!"'])
        self.assertEqual(extract_quotation('"Hello, world!" "Python is awesome!"'), ['"Hello, world!"', '"Python is awesome!"]')
        self.assertEqual(extract_quotation('This is a test. "Hello, world!"'), ['"Hello, world!"'])
        self.assertEqual(extract_quotation('No quotation marks.'), [])
        self.assertEqual(extract_quotation('"Hello, world!" "Python is awesome!" "This is a test."'), ['"Hello, world!"', '"Python is awesome!"', '"This is a test."'])
