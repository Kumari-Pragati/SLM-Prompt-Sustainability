import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count("abc", "a"), 1)
        self.assertEqual(count("abc", "b"), 1)
        self.assertEqual(count("abc", "c"), 1)

    def test_edge_conditions(self):
        self.assertEqual(count("", "a"), 0)
        self.assertEqual(count("a", ""), 0)
        self.assertEqual(count("", ""), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count("a" * 10000, "a"), 10000)
        self.assertEqual(count("b" * 10000, "b"), 10000)
        self.assertEqual(count("c" * 10000, "c"), 10000)

    def test_complex_cases(self):
        self.assertEqual(count("abcabc", "a"), 2)
        self.assertEqual(count("abcabc", "b"), 2)
        self.assertEqual(count("abcabc", "c"), 2)
        self.assertEqual(count("aabbcc", "a"), 2)
        self.assertEqual(count("aabbcc", "b"), 2)
        self.assertEqual(count("aabbcc", "c"), 2)
