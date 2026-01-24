import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_max_occuring_char('aabbbcc'), 'b')

    def test_single_char(self):
        self.assertEqual(get_max_occuring_char('a'), 'a')

    def test_empty_string(self):
        self.assertEqual(get_max_occuring_char(''), '')

    def test_all_same_chars(self):
        self.assertEqual(get_max_occuring_char('aaaaaaa'), 'a')

    def test_edge_case(self):
        self.assertEqual(get_max_occuring_char('123123123'), '1')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_max_occuring_char(123)
