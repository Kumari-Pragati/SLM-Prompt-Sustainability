import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(rearange_string("aabbcc"), "aabbc")

    def test_edge_case1(self):
        self.assertEqual(rearange_string("abc"), "abc")

    def test_edge_case2(self):
        self.assertEqual(rearange_string("aaabbb"), "aabbb")

    def test_edge_case3(self):
        self.assertEqual(rearange_string(""), "")

    def test_edge_case4(self):
        self.assertEqual(rearange_string("a"), "a")

    def test_edge_case5(self):
        self.assertEqual(rearange_string("aa"), "aa")

    def test_edge_case6(self):
        self.assertEqual(rearange_string("abcabc"), "abcabc")

    def test_edge_case7(self):
        self.assertEqual(rearange_string("aabbccdd"), "aabbcdd")

    def test_edge_case8(self):
        self.assertEqual(rearange_string("aabbccddaa"), "aabbcddaa")

    def test_edge_case9(self):
        self.assertEqual(rearange_string("aabbccddaaab"), "aabbcddaaab")

    def test_edge_case10(self):
        self.assertEqual(rearange_string("aabbccddaaabbb"), "aabbcddaaabbb")

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            rearange_string(None)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            rearange_string(123)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            rearange_string([1, 2, 3])

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            rearange_string({"a": 1, "b": 2})
