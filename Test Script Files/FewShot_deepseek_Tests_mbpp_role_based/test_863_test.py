import unittest
from mbpp_863_code import find_longest_conseq_subseq

class TestFindLongestConseqSubseq(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 9, 3, 10, 4, 20, 2]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 4)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 1)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 0)

    def test_boundary_case_repeated_elements(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 1)

    def test_typical_case_with_duplicates(self):
        arr = [2, 4, 3, 1, 10, 5, 9]
        n = len(arr)
        self.assertEqual(find_longest_conseq_subseq(arr, n), 4)

    def test_error_handling_non_integer_elements(self):
        arr = [1, 'a', 3, 4, 5]
        n = len(arr)
        with self.assertRaises(TypeError):
            find_longest_conseq_subseq(arr, n)
