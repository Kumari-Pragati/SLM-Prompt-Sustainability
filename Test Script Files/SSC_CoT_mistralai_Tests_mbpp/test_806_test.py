import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(max_run_uppercase("HELLO"), 5)
        self.assertEqual(max_run_uppercase("WORLD"), 1)
        self.assertEqual(max_run_uppercase("MIXEDCASE"), 3)

    def test_edge_cases(self):
        self.assertEqual(max_run_uppercase(""), 0)
        self.assertEqual(max_run_uppercase("A"), 1)
        self.assertEqual(max_run_uppercase("Z"), 1)
        self.assertEqual(max_run_uppercase("a"), 0)
        self.assertEqual(max_run_uppercase("z"), 0)

    def test_boundary_cases(self):
        self.assertEqual(max_run_uppercase("AaBbCc"), 3)
        self.assertEqual(max_run_uppercase("ZzAa"), 2)
        self.assertEqual(max_run_uppercase("aBbCc"), 0)
        self.assertEqual(max_run_uppercase("Zz"), 1)
