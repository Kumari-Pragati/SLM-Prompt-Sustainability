import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_run_uppercase("ABC"), 3)
        self.assertEqual(max_run_uppercase("AaBbCc"), 0)
        self.assertEqual(max_run_uppercase("ABCabc"), 3)

    def test_edge_conditions(self):
        self.assertEqual(max_run_uppercase(""), 0)
        self.assertEqual(max_run_uppercase("A"), 1)
        self.assertEqual(max_run_uppercase("a"), 0)
        self.assertEqual(max_run_uppercase("123"), 0)

    def test_complex_cases(self):
        self.assertEqual(max_run_uppercase("ABCD"), 1)
        self.assertEqual(max_run_uppercase("ABCDabcd"), 1)
        self.assertEqual(max_run_uppercase("ABCDABCD"), 2)
        self.assertEqual(max_run_uppercase("ABCDABCDabcd"), 2)
        self.assertEqual(max_run_uppercase("AABCDABCD"), 2)
        self.assertEqual(max_run_uppercase("AABCDABCDabcd"), 2)
