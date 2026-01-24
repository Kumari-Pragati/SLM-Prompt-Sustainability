import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearange_string("aab"), "aba")

    def test_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_single_character(self):
        self.assertEqual(rearange_string("a"), "a")

    def test_equal_characters(self):
        self.assertEqual(rearange_string("aaab"), "aaa")

    def test_edge_case_with_most_frequent_character(self):
        self.assertEqual(rearange_string("aabbcc"), "abcabc")

    def test_boundary_case_with_most_frequent_character(self):
        self.assertEqual(rearange_string("aabbccdd"), "abcdabcd")

    def test_corner_case_with_most_frequent_character(self):
        self.assertEqual(rearange_string("aabbccdde"), "abcdeabcde")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rearange_string(123)
