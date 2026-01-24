import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_char('aabbbcc'), 'b')

    def test_single_char(self):
        self.assertEqual(max_char('aaaaa'), 'a')

    def test_empty_string(self):
        self.assertIsNone(max_char(''))

    def test_edge_case_multiple_max_chars(self):
        self.assertEqual(max_char('aabbbccc'), 'c')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_char(12345)
