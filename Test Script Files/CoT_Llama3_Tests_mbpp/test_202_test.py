import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_even("abcdef"), "bd")

    def test_edge_case_empty(self):
        self.assertEqual(remove_even(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_even("a"), "a")

    def test_edge_case_single_even(self):
        self.assertEqual(remove_even("even"), "")

    def test_edge_case_single_odd(self):
        self.assertEqual(remove_even("odd"), "odd")

    def test_edge_case_multiple_even(self):
        self.assertEqual(remove_even("eveneven"), "")

    def test_edge_case_multiple_odd(self):
        self.assertEqual(remove_even("oddodd"), "oddodd")

    def test_edge_case_mixed(self):
        self.assertEqual(remove_even("evenodd"), "od")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_even(123)

    def test_invalid_input_non_string_empty(self):
        with self.assertRaises(TypeError):
            remove_even(None)
