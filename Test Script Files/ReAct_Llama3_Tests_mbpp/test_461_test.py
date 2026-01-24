import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(upper_ctr(""), 0)

    def test_all_uppercase(self):
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_all_lowercase(self):
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_mixed_case(self):
        self.assertEqual(upper_ctr("aAbBcC"), 3)

    def test_non_alpha_chars(self):
        self.assertEqual(upper_ctr("abc123!@#"), 3)

    def test_single_char(self):
        self.assertEqual(upper_ctr("A"), 1)

    def test_no_uppercase(self):
        self.assertEqual(upper_ctr("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_no_lowercase(self):
        self.assertEqual(upper_ctr("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_empty_string_return(self):
        with self.assertRaises(TypeError):
            upper_ctr()
