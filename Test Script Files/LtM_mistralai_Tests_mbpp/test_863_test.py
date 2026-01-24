import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(find_longest_conseq_subseq([1, 1, 1, 3, 4, 5], 6), 4)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6], 6), 6)

    def test_edge_case(self):
        self.assertEqual(find_longest_conseq_subseq([1, 1, 1, 0, 1, 1, 1], 7), 4)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 0, 5], 6), 4)
        self.assertEqual(find_longest_conseq_subseq([0, 0, 0, 0, 0, 0], 6), 1)

    def test_boundary_case(self):
        self.assertEqual(find_longest_conseq_subseq([-10, -9, -8, -7, -6], 5), 5)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 0), 0)
