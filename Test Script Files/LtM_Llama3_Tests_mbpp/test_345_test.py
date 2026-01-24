import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_single_element_input(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_two_element_input(self):
        self.assertEqual(diff_consecutivenums([1, 2]), [1])

    def test_multiple_elements_input(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_negative_numbers_input(self):
        self.assertEqual(diff_consecutivenums([-1, -2, -3, -4, -5]), [-1, -1, -1])

    def test_mixed_positive_and_negative_numbers_input(self):
        self.assertEqual(diff_consecutivenums([1, -2, 3, -4, 5]), [3, -7, 9])

    def test_large_numbers_input(self):
        self.assertEqual(diff_consecutivenums([100, 200, 300, 400, 500]), [100, 100, 100])

    def test_edge_case_input(self):
        self.assertEqual(diff_consecutivenums([1, 1, 1, 1, 1]), [])
