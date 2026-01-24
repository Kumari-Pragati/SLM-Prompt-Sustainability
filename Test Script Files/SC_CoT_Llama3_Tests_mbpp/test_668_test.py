import unittest
from mbpp_668_code import replace

class TestReplaceFunction(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(replace("Hello, world! world!", "o"), "Hello, world! world!")

    def test_edge_case_single_char(self):
        self.assertEqual(replace("Hello, world!", "o"), "Hello, world!")

    def test_edge_case_no_occurrences(self):
        self.assertEqual(replace("Hello, world!", "x"), "Hello, world!")

    def test_edge_case_no_pattern(self):
        self.assertEqual(replace("Hello, world!", ""), "Hello, world!")

    def test_edge_case_pattern_at_end(self):
        self.assertEqual(replace("Hello, world! world!", "o"), "Hello, world! world!")

    def test_edge_case_pattern_at_start(self):
        self.assertEqual(replace("world! Hello, world!", "o"), "world! Hello, world!")

    def test_edge_case_pattern_in_middle(self):
        self.assertEqual(replace("Hello, world! world! world!", "o"), "Hello, world! world! world!")

    def test_edge_case_pattern_multiple_occurrences(self):
        self.assertEqual(replace("Hello, world! world! world! world!", "o"), "Hello, world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_single_char(self):
        self.assertEqual(replace("Hello, world! world! world! world! world!", "o"), "Hello, world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_no_occurrences(self):
        self.assertEqual(replace("Hello, world! world! world! world! world!", "x"), "Hello, world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_no_pattern(self):
        self.assertEqual(replace("Hello, world! world! world! world! world!", ""), "Hello, world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_at_end(self):
        self.assertEqual(replace("Hello, world! world! world! world! world!", "o"), "Hello, world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_at_start(self):
        self.assertEqual(replace("world! Hello, world! world! world! world! world!", "o"), "world! Hello, world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world!", "o"), "Hello, world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_single_char(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world!", "o"), "Hello, world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_no_occurrences(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world!", "x"), "Hello, world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_no_pattern(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world!", ""), "Hello, world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_pattern_at_end(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world!", "o"), "Hello, world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_pattern_at_start(self):
        self.assertEqual(replace("world! Hello, world! world! world! world! world! world!", "o"), "world! Hello, world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_pattern_in_middle(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world! world!", "o"), "Hello, world! world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_pattern_in_middle_and_single_char(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world! world!", "o"), "Hello, world! world! world! world! world! world! world!")

    def test_edge_case_pattern_multiple_occurrences_and_pattern_in_middle_and_pattern_in_middle_and_no_occurrences(self):
        self.assertEqual(replace("Hello, world! world! world! world! world! world! world!", "x"),