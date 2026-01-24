import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Char("aabbb", "b"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Char("", "a"), 0)

    def test_boundary_case_single_char(self):
        self.assertEqual(count_Char("a", "a"), 10)

    def test_boundary_case_long_string(self):
        self.assertEqual(count_Char("a"*10000, "a"), 100000)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            count_Char(None, "a")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            count_Char(123, "a")

    def test_invalid_input_non_char(self):
        with self.assertRaises(TypeError):
            count_Char("abc", 1)
