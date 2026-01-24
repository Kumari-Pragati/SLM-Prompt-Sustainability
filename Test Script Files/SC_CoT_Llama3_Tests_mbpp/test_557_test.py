import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")

    def test_edge_case_empty_string(self):
        self.assertEqual(toggle_string(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(toggle_string("a"), "A")

    def test_edge_case_all_uppercase(self):
        self.assertEqual(toggle_string("UPPERCASE"), "UPPERCASE")

    def test_edge_case_all_lowercase(self):
        self.assertEqual(toggle_string("lowercase"), "lowercase")

    def test_edge_case_mixed_case(self):
        self.assertEqual(toggle_string("Mixed Case"), "mIxEd CaSe")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            toggle_string(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            toggle_string(None)
