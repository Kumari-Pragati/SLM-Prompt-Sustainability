import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(upper_ctr("HelloWorld"), 2)

    def test_edge_case_all_upper(self):
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_edge_case_all_lower(self):
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_edge_case_mixed(self):
        self.assertEqual(upper_ctr("HelloWorld123"), 2)

    def test_edge_case_empty(self):
        self.assertEqual(upper_ctr(""), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(upper_ctr("A"), 1)

    def test_edge_case_single_char_lower(self):
        self.assertEqual(upper_ctr("a"), 0)

    def test_edge_case_single_char_non_alpha(self):
        self.assertEqual(upper_ctr("1"), 0)

    def test_edge_case_non_alpha_string(self):
        self.assertEqual(upper_ctr("123456"), 0)

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            upper_ctr(123)
