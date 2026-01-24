import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_run_uppercase("ABCDE"), 5)

    def test_edge_case(self):
        self.assertEqual(max_run_uppercase(""), 0)

    def test_boundary_case(self):
        self.assertEqual(max_run_uppercase("A"), 1)
        self.assertEqual(max_run_uppercase("a"), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_run_uppercase(123)
        with self.assertRaises(TypeError):
            max_run_uppercase(["A", "B", "C"])

    def test_mixed_case(self):
        self.assertEqual(max_run_uppercase("ABCDabcde"), 4)
        self.assertEqual(max_run_uppercase("ABCDabcdeFGH"), 4)
        self.assertEqual(max_run_uppercase("ABCDabcdeFGHIJK"), 5)
