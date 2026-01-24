import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(extract_values('"string1" "string2" "string3"'), ['string1', 'string2', 'string3'])

    def test_edge_case_empty_string(self):
        self.assertListEqual(extract_values(''), [])

    def test_edge_case_single_string(self):
        self.assertListEqual(extract_values('"string"'), ['string'])

    def test_edge_case_no_quotes(self):
        self.assertListEqual(extract_values('string'), [])

    def test_edge_case_escaped_quotes(self):
        self.assertListEqual(extract_values('"string with \"escaped\" quotes"'), ['string with "escaped" quotes'])

    def test_edge_case_multiple_spaces(self):
        self.assertListEqual(extract_values('" string1 " " string2 " "'), ['string1', 'string2'])

    def test_edge_case_trailing_spaces(self):
        self.assertListEqual(extract_values('"string"   '), ['string'])

    def test_edge_case_leading_spaces(self):
        self.assertListEqual(extract_values('   "string"'), ['string'])
