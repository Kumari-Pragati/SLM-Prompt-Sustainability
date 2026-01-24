import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")

    def test_edge_case_upper(self):
        self.assertEqual(toggle_string("ALLCAPS"), "allcaps")

    def test_edge_case_lower(self):
        self.assertEqual(toggle_string("alllower"), "ALLlower")

    def test_edge_case_mixed(self):
        self.assertEqual(toggle_string("mixedCase"), "MiXeDcAsE")

    def test_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_single_character(self):
        self.assertEqual(toggle_string("a"), "A")

    def test_empty_string_return(self):
        self.assertEqual(toggle_string(""), "")
