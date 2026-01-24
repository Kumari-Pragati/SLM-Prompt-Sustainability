import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearange_string("aab"), "aba")

    def test_edge_case(self):
        self.assertEqual(rearange_string("aaab"), "")
        self.assertEqual(rearange_string("a"), "a")
        self.assertEqual(rearange_string(""), "")

    def test_corner_case(self):
        self.assertEqual(rearange_string("aaabbb"), "ababab")
        self.assertEqual(rearange_string("aabb"), "abab")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rearange_string(123)
        with self.assertRaises(TypeError):
            rearange_string(None)
        with self.assertRaises(TypeError):
            rearange_string(True)
        with self.assertRaises(TypeError):
            rearange_string(["a", "b", "c"])
