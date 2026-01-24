import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_edge_case_single_element(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(diff_consecutivenums([1, 1]), [])

    def test_edge_case_three_element_list(self):
        self.assertEqual(diff_consecutivenums([1, 1, 1]), [])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, 0, 1]), [1, -1])

    def test_edge_case_positive_and_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, 0, 1, 2, 3]), [1, -1, 2, 1])

    def test_edge_case_repeated_numbers(self):
        self.assertEqual(diff_consecutivenums([1, 1, 2, 2, 3, 3]), [1, 0, 0, 1])

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5, 6]), [1, 1, 1, 1])

    def test_edge_case_large_numbers(self):
        self.assertEqual(diff_consecutivenums([100, 101, 102, 103, 104, 105]), [1, 1, 1, 1])

    def test_edge_case_negative_large_numbers(self):
        self.assertEqual(diff_consecutivenums([-100, -99, -98, -97, -96, -95]), [1, 1, 1, 1])

    def test_edge_case_mixed_negative_and_positive_large_numbers(self):
        self.assertEqual(diff_consecutivenums([-100, -99, -98, -97, -96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1