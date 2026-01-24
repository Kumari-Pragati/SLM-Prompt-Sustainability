import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4], 4), 4)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(find_longest_conseq_subseq([5, 4, 3, 2, 1], 5), 5)

    def test_edge_conditions(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)
        self.assertEqual(find_longest_conseq_subseq([1, 1, 1, 1], 4), 1)

    def test_boundary_conditions(self):
        self.assertEqual(find_longest_conseq_subseq([1000, 2000, 3000, 4000], 4), 4)
        self.assertEqual(find_longest_conseq_subseq([-1000, -999, -998, -997], 4), 4)

    def test_complex_cases(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 6, 7, 8], 6), 3)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 8, 9, 10], 8), 5)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 10)
