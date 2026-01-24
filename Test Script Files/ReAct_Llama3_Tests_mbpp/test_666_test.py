import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char('', 'o'), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count_char('a', 'a'), 1)

    def test_edge_case_single_char_string_no_match(self):
        self.assertEqual(count_char('a', 'b'), 0)

    def test_edge_case_multiple_char_string(self):
        self.assertEqual(count_char('hello', 'l'), 2)

    def test_edge_case_multiple_char_string_no_match(self):
        self.assertEqual(count_char('hello', 'z'), 0)

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            count_char(123, 'o')

    def test_edge_case_non_string_input2(self):
        with self.assertRaises(TypeError):
            count_char('hello', 123)
