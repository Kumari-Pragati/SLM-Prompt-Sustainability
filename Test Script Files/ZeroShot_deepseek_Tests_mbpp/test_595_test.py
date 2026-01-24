import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_min_swaps(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)
        self.assertEqual(min_Swaps('abcd', 'bcda'), 1)
        self.assertEqual(min_Swaps('abcd', 'abcd'), 0)
        self.assertEqual(min_Swaps('abc', 'abc'), 0)
        self.assertEqual(min_Swaps('abc', 'def'), "Not Possible")
