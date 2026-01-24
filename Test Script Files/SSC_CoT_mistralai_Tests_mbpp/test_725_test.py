import unittest
from mbpp_725_code import extract_quotation

class TestExtractQuotation(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(extract_quotation('He said, "I love Python"'), ['I love Python'])
        self.assertListEqual(extract_quotation('She said, "I don't like Python"'), ['I don\'t like Python'])

    def test_edge_cases(self):
        self.assertListEqual(extract_quotation('He said, "I love  Python"'), ['I love  Python'])
        self.assertListEqual(extract_quotation('He said, "I love Python, too!"'), ['I love Python, too!'])
        self.assertListEqual(extract_quotation('He said, "I love Python" and "I love Java"'), [])
        self.assertListEqual(extract_quotation('He said, "I love Python" "I love Java"'), [])
        self.assertListEqual(extract_quotation('"I love Python"'), ['I love Python'])
        self.assertListEqual(extract_quotation('"I love Python" "I love Java"'), ['I love Python', 'I love Java'])

    def test_invalid_input(self):
        self.assertListEqual(extract_quotation('He said, 123'), [])
        self.assertListEqual(extract_quotation('He said, "I love Python" "I love Java" 123'), [])
        self.assertListEqual(extract_quotation('"I love Python" 123'), [])
