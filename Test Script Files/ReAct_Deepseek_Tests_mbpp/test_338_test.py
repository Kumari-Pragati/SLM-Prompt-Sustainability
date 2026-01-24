import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abccba"), 10)
        self.assertEqual(count_Substring_With_Equal_Ends("aabbcc"), 6)
        self.assertEqual(count_Substring_With_Equal_Ends("abcabc"), 6)

    def test_edge_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 2)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(123)
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(["a", "b", "c"])
