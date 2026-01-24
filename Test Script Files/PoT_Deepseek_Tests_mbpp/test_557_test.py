import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")
        self.assertEqual(toggle_string("Python is FUN"), "pYTHON IS fun")

    def test_edge_cases(self):
        self.assertEqual(toggle_string(""), "")
        self.assertEqual(toggle_string("12345"), "12345")

    def test_boundary_cases(self):
        self.assertEqual(toggle_string("a"), "A")
        self.assertEqual(toggle_string("A"), "a")

    def test_corner_cases(self):
        self.assertEqual(toggle_string("!@#$%^&*()"), "!@#$%^&*()")
        self.assertEqual(toggle_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "abcdefghijklmnopqrstuvwxyz")
