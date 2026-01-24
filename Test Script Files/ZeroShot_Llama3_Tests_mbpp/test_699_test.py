import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_min_swaps(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)
        self.assertEqual(min_Swaps("abc", "def"), 3)
        self.assertEqual(min_Swaps("abc", "abcd"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "defg"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "abcd"), 1)
        self.assertEqual(min_Swaps("abc", "defg"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "abcde"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "abcdf"), 2)
        self.assertEqual(min_Swaps("abc", "abcdef"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "abcdefg"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "abcdefh"), "Not Possible")
        self.assertEqual(min_Swaps("abc", "abcdefgh"), "Not Possible")
