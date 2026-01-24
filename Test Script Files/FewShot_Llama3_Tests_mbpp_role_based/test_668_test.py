import unittest
from mbpp_668_code import replace

class TestReplace(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace("Hello, world! world!", "o"), "Hello, world! world!")

    def test_edge_case_single_char(self):
        self.assertEqual(replace("Hello, world!", "o"), "Hello, world!")

    def test_edge_case_no_matches(self):
        self.assertEqual(replace("Hello, world!", "x"), "Hello, world!")

    def test_edge_case_multiple_matches(self):
        self.assertEqual(replace("Hello, world! world! world!", "o"), "Hello, world! world! world!")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace("", "o"), "")

    def test_edge_case_single_char_no_matches(self):
        self.assertEqual(replace("Hello, world!", "z"), "Hello, world!")

    def test_edge_case_single_char_multiple_matches(self):
        self.assertEqual(replace("Hello, world! world! world!", "o"), "Hello, world! world! world!")
