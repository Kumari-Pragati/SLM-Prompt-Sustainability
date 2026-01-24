import unittest
from mbpp_437_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_odd("abcdef"), "acef")

    def test_edge_case_empty(self):
        self.assertEqual(remove_odd(""), "")

    def test_edge_case_single_char(self):
        self.assertEqual(remove_odd("a"), "a")

    def test_edge_case_even_length(self):
        self.assertEqual(remove_odd("abcdef"), "acef")

    def test_edge_case_odd_length(self):
        self.assertEqual(remove_odd("abcdefg"), "acefg")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_odd(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_odd(None)
