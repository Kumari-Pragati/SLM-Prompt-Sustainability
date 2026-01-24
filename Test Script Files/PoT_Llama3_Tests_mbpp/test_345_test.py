import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(diff_consecutivenums([1, 1]), [])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, 0, 1]), [1])

    def test_edge_case_non_integer_numbers(self):
        self.assertEqual(diff_consecutivenums([1.0, 2.0, 3.0]), [1.0])

    def test_edge_case_mixed_types(self):
        self.assertEqual(diff_consecutivenums([1, 'a', 3]), [2])

    def test_edge_case_non_consecutive_numbers(self):
        self.assertEqual(diff_consecutivenums([1, 3, 5, 7]), [2, 2])
