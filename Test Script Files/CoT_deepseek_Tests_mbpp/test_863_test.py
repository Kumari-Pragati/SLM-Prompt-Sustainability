import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 9, 3, 10, 4, 20, 2]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 4)

    def test_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 1)

    def test_no_consecutive_elements(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 7)

    def test_consecutive_elements(self):
        arr = [2, 3, 4, 5, 6, 7, 8]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 7)

    def test_duplicate_elements(self):
        arr = [1, 9, 3, 10, 4, 20, 2, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 5)

    def test_negative_elements(self):
        arr = [-1, -3, -4, 0, 1, 2, 3]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 4)

    def test_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 0)
