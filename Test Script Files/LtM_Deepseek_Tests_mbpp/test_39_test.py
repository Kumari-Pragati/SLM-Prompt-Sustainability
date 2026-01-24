import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_input(self):
        self.assertEqual(rearange_string("aab"), "aba")
        self.assertEqual(rearange_string("aaab"), "abab")

    # Test for edge and boundary conditions
    def test_edge_cases(self):
        self.assertEqual(rearange_string(""), "")
        self.assertEqual(rearange_string("a"), "a")
        self.assertEqual(rearange_string("aa"), "aa")
        self.assertEqual(rearange_string("aaa"), "aaa")

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(rearange_string("aabb"), "abab")
        self.assertEqual(rearange_string("aaabbb"), "ababab")
        self.assertEqual(rearange_string("aaabbbcc"), "abcabcab")
        self.assertEqual(rearange_string("aaabbbccdd"), "abcdabcd")

    # Test for invalid inputs
    def test_invalid_inputs(self):
        self.assertEqual(rearange_string("aabbccddeeff"), "")
        self.assertEqual(rearange_string("aabbccddeeffg"), "")
