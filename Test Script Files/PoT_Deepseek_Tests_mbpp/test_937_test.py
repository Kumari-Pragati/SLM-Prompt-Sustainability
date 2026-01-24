import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_char('aabbbcc'), 'b')

    def test_edge_case_single_char(self):
        self.assertEqual(max_char('a'), 'a')

    def test_boundary_case_empty_string(self):
        self.assertIsNone(max_char(''))

    def test_corner_case_repeated_chars(self):
        self.assertEqual(max_char('aaabbbccc'), 'a')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_char(12345)
