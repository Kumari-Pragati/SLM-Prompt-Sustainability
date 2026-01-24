import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_find_longest_conseq_subseq(self):
        self.assertEqual(find_longest_conseq_subseq([1, 9, 3, 10, 4, 20, 2], 7), 4)
        self.assertEqual(find_longest_conseq_subseq([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11), 5)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 10)
        self.assertEqual(find_longest_conseq_subseq([100, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 10)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 3, 2, 3, 4, 5], 10), 5)
