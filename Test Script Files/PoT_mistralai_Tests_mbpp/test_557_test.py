import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(toggle_string("Hello, World!"), "hELLO, wRLD!")

    def test_edge_case_uppercase(self):
        self.assertEqual(toggle_string("HELLO, WORLD!"), "hello, world!")

    def test_edge_case_lowercase(self):
        self.assertEqual(toggle_string("hello, world!"), "HELLO, WORLD!")

    def test_boundary_case_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_boundary_case_single_char(self):
        self.assertEqual(toggle_string("A"), "a")
