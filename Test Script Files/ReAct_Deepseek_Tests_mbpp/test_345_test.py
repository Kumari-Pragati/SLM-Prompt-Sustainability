import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4]), [1, 1])

    def test_single_element(self):
        self.assertEqual(diff_consecutivenums([1]), [])

    def test_empty_list(self):
        self.assertEqual(diff_consecutivenums([]), [])

    def test_negative_numbers(self):
        self.assertEqual(diff_consecutivenums([-1, -2, -3, -4]), [-1, -1])

    def test_zeroes(self):
        self.assertEqual(diff_consecutivenums([0, 0, 0, 0]), [0, 0])

    def test_large_numbers(self):
        self.assertEqual(diff_consecutivenums([1000, 2000, 3000, 4000]), [1000, 1000])

    def test_decimal_numbers(self):
        self.assertEqual(diff_consecutivenums([1.1, 2.2, 3.3, 4.4]), [1.1, 1.1])

    def test_mixed_numbers(self):
        self.assertEqual(diff_consecutivenums([1, 2.2, 3, 4.4]), [1.2, 1.2])

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums(['1', '2', '3', '4'])

    def test_none_list(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums(None)
