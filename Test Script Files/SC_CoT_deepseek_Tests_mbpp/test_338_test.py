import unittest

from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcab"), 2)
        self.assertEqual(count_Substring_with_equal_ends("aabbaa"), 4)

    def test_edge_cases(self):
        self.assertEqual(count_Substring_with_equal_ends(""), 0)
        self.assertEqual(count_Substring_with_equal_ends("a"), 1)

    def test_corner_cases(self):
        self.assertEqual(count_Substring_with_equal_ends("aaaaa"), 10)
        self.assertEqual(count_Substring_with_equal_ends("ababab"), 9)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Substring_with_equal_ends(123)
        with self.assertRaises(TypeError):
            count_Substring_with_equal_ends(["a", "b", "c"])
