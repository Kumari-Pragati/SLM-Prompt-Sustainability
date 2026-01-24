import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_run_uppercase("ABCDEF"), 6)

    def test_edge_case_no_uppercase(self):
        self.assertEqual(max_run_uppercase("abcdef"), 0)

    def test_edge_case_all_uppercase(self):
        self.assertEqual(max_run_uppercase("ABCDEFGH"), 8)

    def test_edge_case_single_uppercase(self):
        self.assertEqual(max_run_uppercase("aBcDeFgHi"), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(max_run_uppercase(""), 0)

    def test_edge_case_single_character_uppercase(self):
        self.assertEqual(max_run_uppercase("A"), 1)

    def test_edge_case_single_character_lowercase(self):
        self.assertEqual(max_run_uppercase("a"), 0)
