import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_run_uppercase("ABCDEF"), 6)
        self.assertEqual(max_run_uppercase("ABCDabc"), 4)
        self.assertEqual(max_run_uppercase("ABCDEfGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_run_uppercase(""), 0)
        self.assertEqual(max_run_uppercase("abcdef"), 0)
        self.assertEqual(max_run_uppercase("ABCDEFabcdef"), 6)

    def test_corner_cases(self):
        self.assertEqual(max_run_uppercase("ABCDEfGHIJKLMNOPQRSTUVWXYZabcdef"), 26)
        self.assertEqual(max_run_uppercase("ABCDEfGHIJKLMNOPQRSTUVWXYZabc"), 26)
        self.assertEqual(max_run_uppercase("ABCDEfGHIJKLMNOPQRSTUVWXYZabcDEF"), 26)
