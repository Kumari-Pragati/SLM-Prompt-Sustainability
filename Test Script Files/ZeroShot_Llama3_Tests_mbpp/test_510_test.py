import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_no_of_subsequences(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 2)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4], 4), 3)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5, 6], 6, 0), 0)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5, 6], 6, 1), 1)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5, 6], 6, 2), 2)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5, 6], 6, 3), 3)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5, 6], 6, 4), 4)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5, 6], 6, 5), 5)
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5, 6], 6, 6), 6)
