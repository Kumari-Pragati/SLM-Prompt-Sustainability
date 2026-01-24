import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_no_of_subsequences(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 10), 6)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 15), 10)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 20), 14)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 25), 16)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 30), 18)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 0), 1)
        self.assertEqual(no_of_subsequences([], 10), 0)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], -10), 0)
