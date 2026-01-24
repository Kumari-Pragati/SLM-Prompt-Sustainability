import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_run_uppercase("HelloWORLD"), 2)

    def test_single_uppercase(self):
        self.assertEqual(max_run_uppercase("H"), 1)

    def test_all_uppercase(self):
        self.assertEqual(max_run_uppercase("HELLO"), 1)

    def test_all_lowercase(self):
        self.assertEqual(max_run_uppercase("hello"), 0)

    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(""), 0)

    def test_edge_case_start_uppercase(self):
        self.assertEqual(max_run_uppercase("AaBbCc"), 3)

    def test_edge_case_end_uppercase(self):
        self.assertEqual(max_run_uppercase("aabbccD"), 3)

    def test_edge_case_all_uppercase(self):
        self.assertEqual(max_run_uppercase("ABCDEF"), 1)

    def test_edge_case_all_lowercase(self):
        self.assertEqual(max_run_uppercase("abcdef"), 0)

    def test_special_case_mixed_case(self):
        self.assertEqual(max_run_uppercase("AbCDeFg"), 2)

    def test_special_case_mixed_case_2(self):
        self.assertEqual(max_run_uppercase("aBCDeFG"), 2)
