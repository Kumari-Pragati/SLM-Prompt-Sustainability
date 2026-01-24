import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1, 1])

    def test_edge_case_empty_list(self):
        self.assertListEqual(diff_consecutivenums([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(diff_consecutivenums([1]), [])

    def test_edge_case_two_elements(self):
        self.assertListEqual(diff_consecutivenums([1, 2]), [1])

    def test_boundary_case_first_element(self):
        self.assertListEqual(diff_consecutivenums([1]), [])

    def test_boundary_case_last_element(self):
        self.assertListEqual(diff_consecutivenums([1, 2, 3]), [2])
