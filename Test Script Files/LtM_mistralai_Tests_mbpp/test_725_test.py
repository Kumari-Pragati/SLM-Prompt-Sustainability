import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_simple_quotes(self):
        self.assertListEqual(extract_quotation('"Hello, World!"'), ['Hello, World!'])
        self.assertListEqual(extract_quotation('"This is a test"'), ['This is a test'])

    def test_multiple_quotes(self):
        self.assertListEqual(extract_quotation('"Hello, World!", "This is a test"'),
                              ['Hello, World!', 'This is a test'])
        self.assertListEqual(extract_quotation('"Hello, World!", "This is a test", "Another quote"'),
                              ['Hello, World!', 'This is a test', 'Another quote'])

    def test_empty_string(self):
        self.assertListEqual(extract_quotation(''), [])

    def test_no_quotes(self):
        self.assertListEqual(extract_quotation('Hello, World!'), [])

    def test_escaped_quotes(self):
        self.assertListEqual(extract_quotation('"This is a \"test\" with escaped quotes"'),
                              ['This is a "test" with escaped quotes'])

    def test_quotes_with_special_characters(self):
        self.assertListEqual(extract_quotation('"This is a test with #@$%^&*()_+-=[]{}|;:\"\'<>,.?/ ~"'),
                              ['This is a test with #@$%^&*()_+-=[]{}|;:\"\'<>,.?/ ~'])

    def test_quotes_with_newlines(self):
        self.assertListEqual(extract_quotation('"This is a\nnew line test"'), ['This is a new line test'])
