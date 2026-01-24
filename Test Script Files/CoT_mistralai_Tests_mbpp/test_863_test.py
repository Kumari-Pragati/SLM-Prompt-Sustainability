import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_longest_conseq_subseq([1], 1), 1)

    def test_consecutive_positive_numbers(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3, 4, 5, 6, 7], 7), 7)

    def test_consecutive_negative_numbers(self):
        self.assertEqual(find_longest_conseq_subseq([-1, -2, -3, -4, -5, -6, -7], 7), 7)

    def test_consecutive_positive_and_negative_numbers(self):
        self.assertEqual(find_longest_conseq_subseq([1, -2, 3, -4, 5, -6, 7], 7), 5)

    def test_duplicates(self):
        self.assertEqual(find_longest_conseq_subseq([1, 1, 2, 1, 3, 1, 4, 1, 5], 9), 6)

    def test_unsorted_list(self):
        self.assertEqual(find_longest_conseq_subseq([5, 3, 4, 2, 1], 5), 4)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            find_longest_conseq_subseq([1, 2, 3], -1)

    def test_zero_n(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3], 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_longest_conseq_subseq('abc', 10)
