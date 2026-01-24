import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count("hello", "l"), 3)
        self.assertEqual(count("Python", "n"), 1)
        self.assertEqual(count("12345", "5"), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(count("", "a"), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(count("a", "a"), 1)

    def test_edge_case_single_char_input(self):
        self.assertEqual(count("hello", "z"), 0)

    def test_corner_case_negative_index(self):
        self.assertRaises(IndexError, lambda: count("-1a", "a"))
