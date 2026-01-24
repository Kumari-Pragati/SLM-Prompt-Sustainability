import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4]), [1, 1])

    def test_single_element(self):
        self.assertEqual(diff_consecutivenums([5]), [])

    def test_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, -2, -3, -4]), [-1, -1])

    def test_large_numbers(self):
        self.assertEqual(diff_consecutivenums([1000, 2000, 3000, 4000]), [1000, 1000])

    def test_decimal_numbers(self):
        self.assertEqual(diff_consecutivenums([1.5, 2.5, 3.5, 4.5]), [1.0, 1.0])

    def test_zero_elements(self):
        self.assertEqual(diff_consecutivenums([0, 0, 0, 0]), [0, 0])

    def test_large_list(self):
        self.assertEqual(diff_consecutivenums(list(range(1, 1001))), list(range(1, 1000)))
