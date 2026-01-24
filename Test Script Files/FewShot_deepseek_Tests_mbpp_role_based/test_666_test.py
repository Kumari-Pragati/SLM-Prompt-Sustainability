import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_char("hello", "l"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_char("", "a"), 0)

    def test_boundary_case_single_char(self):
        self.assertEqual(count_char("a", "a"), 1)
        self.assertEqual(count_char("a", "b"), 0)

    def test_boundary_case_multiple_chars(self):
        self.assertEqual(count_char("aaaa", "a"), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_char(123, "a")
        with self.assertRaises(TypeError):
            count_char("hello", 123)
