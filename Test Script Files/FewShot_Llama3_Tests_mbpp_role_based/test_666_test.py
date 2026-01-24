import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_char("hello", "l"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count_char("a", "a"), 1)

    def test_edge_case_single_char_string_no_match(self):
        self.assertEqual(count_char("a", "b"), 0)

    def test_edge_case_empty_char(self):
        self.assertEqual(count_char("hello", ""), 0)

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            count_char(123, "a")

    def test_edge_case_non_char_input(self):
        with self.assertRaises(TypeError):
            count_char("hello", 123)
