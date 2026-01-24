import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char('hello', 'l'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char('', 'a'), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count_char('a', 'a'), 1)
        self.assertEqual(count_char('a', 'b'), 0)

    def test_edge_case_char_not_in_string(self):
        self.assertEqual(count_char('hello', 'z'), 0)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            count_char(None, 'a')

    def test_invalid_input_non_string_first_argument(self):
        with self.assertRaises(TypeError):
            count_char(123, 'a')

    def test_invalid_input_non_string_second_argument(self):
        with self.assertRaises(TypeError):
            count_char('hello', 123)
