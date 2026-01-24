import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(common_prefix(["flower", "flow", "flight"], 3), "fl")
        self.assertEqual(common_prefix(["dog", "racecar", "car"], 3), "")
        self.assertEqual(common_prefix(["interspecies", "interstellar", "interstate"], 3), "inters")

    def test_edge_cases(self):
        self.assertEqual(common_prefix(["a"], 1), "a")
        self.assertEqual(common_prefix([], 0), "")

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            common_prefix(["flower", "flow", "flight"], "3")
        with self.assertRaises(TypeError):
            common_prefix(["flower", "flow", "flight"], None)
        with self.assertRaises(TypeError):
            common_prefix(["flower", "flow", "flight"], [])
