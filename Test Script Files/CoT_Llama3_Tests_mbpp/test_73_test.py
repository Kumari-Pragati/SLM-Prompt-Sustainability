import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_typical_split(self):
        self.assertEqual(multiple_split("Hello; World, this is a test*"), ["Hello", " World", " this is a test"])

    def test_edge_case_empty_string(self):
        self.assertEqual(multiple_split(""), [])

    def test_edge_case_single_separator(self):
        self.assertEqual(multiple_split("Hello;"), ["Hello"])

    def test_edge_case_multiple_separators(self):
        self.assertEqual(multiple_split("Hello; World, this is a test*"), ["Hello", " World, this is a test"])

    def test_edge_case_multiple_separators_with_spaces(self):
        self.assertEqual(multiple_split("Hello; World, this is a test *"), ["Hello", " World, this is a test "])

    def test_edge_case_multiple_separators_with_newline(self):
        self.assertEqual(multiple_split("Hello; World, this is a test\n"), ["Hello", " World, this is a test"])

    def test_edge_case_multiple_separators_with_all(self):
        self.assertEqual(multiple_split("Hello; World, this is a test * \n"), ["Hello", " World, this is a test"])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            multiple_split(123)
