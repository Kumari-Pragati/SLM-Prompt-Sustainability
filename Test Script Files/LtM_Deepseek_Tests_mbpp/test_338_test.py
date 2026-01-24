import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abccba"), 6)
        self.assertEqual(count_Substring_With_Equal_Ends("aabb"), 4)
        self.assertEqual(count_Substring_With_Equal_Ends("abcba"), 4)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcabc"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 6)
        self.assertEqual(count_Substring_With_Equal_Ends("ababab"), 6)
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefgfedcba"), 12)
