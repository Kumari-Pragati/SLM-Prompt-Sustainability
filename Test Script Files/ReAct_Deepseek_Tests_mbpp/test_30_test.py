import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcab"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("aabbaa"), 4)
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("ababab"), 6)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(123)
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(["a", "b", "c"])
