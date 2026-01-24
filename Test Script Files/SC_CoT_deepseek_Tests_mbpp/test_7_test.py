import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_char_long("Hello world!"), ['Hello', 'world'])

    def test_edge_case_single_char(self):
        self.assertEqual(find_char_long("a"), [])

    def test_edge_case_multiple_chars(self):
        self.assertEqual(find_char_long("ab"), [])

    def test_edge_case_four_chars(self):
        self.assertEqual(find_char_long("abcd"), ['abcd'])

    def test_edge_case_four_chars_with_spaces(self):
        self.assertEqual(find_char_long("abcd "), ['abcd'])

    def test_edge_case_four_chars_with_punctuation(self):
        self.assertEqual(find_char_long("abcd!"), ['abcd'])

    def test_corner_case_special_chars(self):
        self.assertEqual(find_char_long("!@#$"), [])

    def test_corner_case_numbers(self):
        self.assertEqual(find_char_long("123456"), ['123456'])

    def test_corner_case_mixed_chars(self):
        self.assertEqual(find_char_long("abc123"), ['abc123'])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_char_long(123456)
