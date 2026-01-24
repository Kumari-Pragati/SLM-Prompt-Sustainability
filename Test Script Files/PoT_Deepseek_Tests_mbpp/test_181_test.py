import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(common_prefix(["flower", "flow", "flight"], 3), "fl")
        self.assertEqual(common_prefix(["dog", "racecar", "car"], 3), "")
        self.assertEqual(common_prefix(["apple", "apple", "apple"], 3), "apple")

    def test_edge_cases(self):
        self.assertEqual(common_prefix(["a"], 1), "a")
        self.assertEqual(common_prefix([""], 1), "")
        self.assertEqual(common_prefix([], 0), "")

    def test_boundary_cases(self):
        self.assertEqual(common_prefix(["abcdefgh", "abcdefg"], 2), "abcdefg")
        self.assertEqual(common_prefix(["abcdefgh", "abcdefghi"], 2), "abcdefgh")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            common_prefix(123, 3)
        with self.assertRaises(TypeError):
            common_prefix(["apple", "apple", "apple"], "3")
        with self.assertRaises(TypeError):
            common_prefix(["apple", "apple", "apple"], [])
