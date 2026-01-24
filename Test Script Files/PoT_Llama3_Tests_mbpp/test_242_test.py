import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_charac("hello"), 5)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_charac(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(count_charac("a"), 1)

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(count_charac("   "), 3)

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            count_charac(123)

    def test_edge_case_mixed_case(self):
        self.assertEqual(count_charac("Hello"), 5)

    def test_edge_case_punctuation(self):
        self.assertEqual(count_charac("Hello, World!"), 11)
