import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(minimum_Length("aabbcc"), 0)
        self.assertEqual(minimum_Length("abcabc"), 0)
        self.assertEqual(minimum_Length("aaaaaa"), 6)

    def test_edge_conditions(self):
        self.assertEqual(minimum_Length(""), 0)
        self.assertEqual(minimum_Length("a"), 1)
        self.assertEqual(minimum_Length("ab"), 2)

    def test_boundary_conditions(self):
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyz"), 1)
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyza"), 0)

    def test_complex_cases(self):
        self.assertEqual(minimum_Length("aabbccdd"), 2)
        self.assertEqual(minimum_Length("abcabcabc"), 0)
        self.assertEqual(minimum_Length("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), 26)
