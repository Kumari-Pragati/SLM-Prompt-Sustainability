import unittest
from mbpp_461_code import upper_ctr

class TestUpperCtr(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(upper_ctr("HelloWorld"), 2)

    def test_edge_case(self):
        self.assertEqual(upper_ctr("ALLCAPS"), 12)
        self.assertEqual(upper_ctr("allcaps"), 0)
        self.assertEqual(upper_ctr("mixedCase"), 4)
        self.assertEqual(upper_ctr("ALLCAPSMIXED"), 12)

    def test_empty_string(self):
        self.assertEqual(upper_ctr(""), 0)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            upper_ctr(123)

    def test_mixed_case_input(self):
        self.assertEqual(upper_ctr("HeLlO"), 3)

    def test_all_uppercase_input(self):
        self.assertEqual(upper_ctr("ALLCAPS"), 12)

    def test_all_lowercase_input(self):
        self.assertEqual(upper_ctr("allcaps"), 0)
