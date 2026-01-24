import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_single_element_list(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_two_elements_list(self):
        self.assertEqual(diff_consecutivenums([1, 2]), [1])

    def test_three_elements_list(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3]), [1, 1])

    def test_list_with_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, 0, 1]), [-1, 1])

    def test_list_with_zero(self):
        self.assertEqual(diff_consecutivenums([0, 0]), [])

    def test_list_with_duplicates(self):
        self.assertEqual(diff_consecutivenums([1, 1, 2, 2, 3, 3]), [1, 1, 1])
