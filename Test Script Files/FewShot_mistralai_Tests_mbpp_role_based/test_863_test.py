import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6], 6), 6)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7], 7), 7)

    def test_empty_list(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_duplicates(self):
        self.assertEqual(find_longest_conseq_subseq([1, 1, 2, 3, 4, 4, 5], 7), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_longest_conseq_subseq([-1, -2, -3, -4, -5], 5), 1)

    def test_zero(self):
        self.assertEqual(find_longest_conseq_subseq([0, 0, 0, 0, 0], 5), 5)

    def test_out_of_range_input(self):
        with self.assertRaises(IndexError):
            find_longest_conseq_subseq([1, 2, 3], -1)
