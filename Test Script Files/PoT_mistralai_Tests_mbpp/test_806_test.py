import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)
        self.assertEqual(max_run_uppercase("abcdefghijklmnopqrstuvwxyz"), 0)
        self.assertEqual(max_run_uppercase("AbCdEfGhIjKlMnOpQrStUvWxYz"), 9)

    def test_edge_case(self):
        self.assertEqual(max_run_uppercase("A"), 1)
        self.assertEqual(max_run_uppercase("Z"), 1)
        self.assertEqual(max_run_uppercase(""), 0)
        self.assertEqual(max_run_uppercase("Aa"), 1)
        self.assertEqual(max_run_uppercase("Zz"), 1)

    def test_boundary_case(self):
        self.assertEqual(max_run_uppercase("AaBc"), 2)
        self.assertEqual(max_run_uppercase("ZzY"), 2)
        self.assertEqual(max_run_uppercase("AaBcD"), 3)
        self.assertEqual(max_run_uppercase("ZzYxW"), 3)
