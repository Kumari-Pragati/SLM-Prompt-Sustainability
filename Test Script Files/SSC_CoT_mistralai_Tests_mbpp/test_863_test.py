import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 4, 8, 9, 15, 23, 31], 7), 7)
        self.assertEqual(find_longest_conseq_subseq([4, 6, 10, 11, 15, 20], 6), 6)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)

    def test_edge_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 1, 1, 1, 1, 1], 6), 1)
        self.assertEqual(find_longest_conseq_subseq([20, 20, 20, 20, 20, 20], 6), 1)
        self.assertEqual(find_longest_conseq_subseq([-1, -2, -3, -4, -5, -6], 6), 6)

    def test_boundary_input(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 1), 1)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            find_longest_conseq_subseq([], 0)
        with self.assertRaises(ValueError):
            find_longest_conseq_subseq([1], 0)
        with self.assertRaises(ValueError):
            find_longest_conseq_subseq([1, 2], -1)
