import unittest

from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_max_occuring_char('aabbbcc'), 'b')

    def test_edge_case_single_char(self):
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_edge_case_empty_string(self):
        self.assertEqual(get_max_occuring_char(''), '')

    def test_corner_case_repeated_chars(self):
        self.assertEqual(get_max_occuring_char('aabbcc'), 'a')

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            get_max_occuring_char(None)
