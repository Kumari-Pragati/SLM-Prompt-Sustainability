import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(extract_string("abcdefg", 3), ["abc", "def", "gh"])
        self.assertListEqual(extract_string("123456", 2), ["12", "34", "56"])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(extract_string("", 3), [])
        self.assertListEqual(extract_string("a", 3), [])
        self.assertListEqual(extract_string("aaa", 1), ["a"])
        self.assertListEqual(extract_string("123", 5), [])
        self.assertListEqual(extract_string("123", 0), [])

    def test_complex_input(self):
        self.assertListEqual(extract_string("0123456789", 4), ["0123", "4567", "89"])
        self.assertListEqual(extract_string("0123456789", 5), ["01234", "56789"])
        self.assertListEqual(extract_string("0123456789", 6), ["012345", "6789"])
        self.assertListEqual(extract_string("0123456789", 7), ["0123456", "789"])
        self.assertListEqual(extract_string("0123456789", 8), ["01234567", "89"])
        self.assertListEqual(extract_string("0123456789", 9), ["012345678", "9"])
