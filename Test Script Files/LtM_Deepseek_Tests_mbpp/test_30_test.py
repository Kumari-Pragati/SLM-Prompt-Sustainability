import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("aab"), 4)
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 6)

    def test_edge_conditions(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abababab"), 16)
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefgh"), 8)

    def test_complex_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abccba"), 6)
        self.assertEqual(count_Substring_With_Equal_Ends("abcabcabc"), 9)
