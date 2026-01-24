import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_simple_uppercase(self):
        self.assertEqual(max_run_uppercase("ABC"), 3)
        self.assertEqual(max_run_uppercase("ABCDEFG"), 3)

    def test_simple_mixedcase(self):
        self.assertEqual(max_run_uppercase("AbCdEfG"), 1)
        self.assertEqual(max_run_uppercase("AbCdEfGhI"), 1)

    def test_edge_cases(self):
        self.assertEqual(max_run_uppercase(""), 0)
        self.assertEqual(max_run_uppercase("A"), 1)
        self.assertEqual(max_run_uppercase("Z"), 1)
        self.assertEqual(max_run_uppercase("Aa"), 1)
        self.assertEqual(max_run_uppercase("Zz"), 1)

    def test_complex_cases(self):
        self.assertEqual(max_run_uppercase("ABCABC"), 2)
        self.assertEqual(max_run_uppercase("ABCABCDEFG"), 3)
        self.assertEqual(max_run_uppercase("ABCABCDEFGH"), 3)
        self.assertEqual(max_run_uppercase("ABCABCDEFGHI"), 1)
        self.assertEqual(max_run_uppercase("ABCABCDEFGHIJ"), 1)
