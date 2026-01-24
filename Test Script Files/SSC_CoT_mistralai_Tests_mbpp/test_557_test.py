import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")

    def test_edge_and_boundary_cases(self):
        self.assertEqual(toggle_string(""), "")
        self.assertEqual(toggle_string("A"), "a")
        self.assertEqual(toggle_string("ABC"), "aBC")
        self.assertEqual(toggle_string("abc"), "ABC")
        self.assertEqual(toggle_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(toggle_string("abcdefghijklmnopqrstuvwxyz"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_special_cases(self):
        self.assertEqual(toggle_string("123"), "123")
        self.assertEqual(toggle_string("Hello123World"), "hELLO123wORLD")
        self.assertEqual(toggle_string("Hello_World"), "hELLO_wORLD")
        self.assertEqual(toggle_string("Hello-World"), "hELLO-wORLD")
        self.assertEqual(toggle_string("Hello@World"), "hELLO@wORLD")
        self.assertEqual(toggle_string("Hello[World]"), "hELLO[wORLD]")
        self.assertEqual(toggle_string("Hello]World"), "hELLO]wORLD")
