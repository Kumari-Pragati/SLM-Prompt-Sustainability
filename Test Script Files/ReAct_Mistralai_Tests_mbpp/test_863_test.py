import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_longest_conseq_subseq([], 0), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(find_longest_conseq_subseq([num], 1), 1)

    def test_consecutive_positive_numbers(self):
        for num in range(10):
            test_list = list(range(num + 1))
            self.assertEqual(find_longest_conseq_subseq(test_list, num), num)

    def test_consecutive_negative_numbers(self):
        for num in range(10):
            test_list = [-num for _ in range(num + 1)]
            self.assertEqual(find_longest_conseq_subseq(test_list, num), num)

    def test_consecutive_positive_and_negative_numbers(self):
        test_list = list(range(10)) + [-i for i in range(1, 10)]
        self.assertEqual(find_longest_conseq_subseq(test_list, 19), 19)

    def test_duplicates_in_beginning(self):
        test_list = [1, 1, 2, 3, 4, 5]
        self.assertEqual(find_longest_conseq_subseq(test_list, len(test_list)), 1)

    def test_duplicates_in_middle(self):
        test_list = [1, 2, 2, 3, 4, 5]
        self.assertEqual(find_longest_conseq_subseq(test_list, len(test_list)), 2)

    def test_duplicates_at_end(self):
        test_list = [1, 2, 3, 3, 4, 5]
        self.assertEqual(find_longest_conseq_subseq(test_list, len(test_list)), 3)

    def test_negative_n(self):
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3], -1), 0)
        self.assertEqual(find_longest_conseq_subseq([1, 2, 3], -len(test_list)), 0)
