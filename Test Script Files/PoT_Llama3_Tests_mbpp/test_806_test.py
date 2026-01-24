import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_run_uppercase("HelloWorld"), 1)

    def test_edge_case(self):
        self.assertEqual(max_run_uppercase("HelloWorld123"), 1)

    def test_edge_case2(self):
        self.assertEqual(max_run_uppercase("Hello123World"), 2)

    def test_edge_case3(self):
        self.assertEqual(max_run_uppercase("123456789"), 0)

    def test_edge_case4(self):
        self.assertEqual(max_run_uppercase("ABCabc"), 0)

    def test_edge_case5(self):
        self.assertEqual(max_run_uppercase("ABC"), 1)

    def test_edge_case6(self):
        self.assertEqual(max_run_uppercase("abc"), 0)

    def test_edge_case7(self):
        self.assertEqual(max_run_uppercase("ABCABC"), 2)

    def test_edge_case8(self):
        self.assertEqual(max_run_uppercase("abcABC"), 1)

    def test_edge_case9(self):
        self.assertEqual(max_run_uppercase("123ABC"), 1)

    def test_edge_case10(self):
        self.assertEqual(max_run_uppercase("abc123"), 0)
