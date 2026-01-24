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
        self.assertEqual(diff_consecutivenums([0, 0, 0]), [0, 0])

    def test_large_numbers(self):
        self.assertEqual(diff_consecutivenums(list(range(1, 100))), list(range(1, 99)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            diff_consecutivenums("1, 2, 3, 4")

        with self.assertRaises(TypeError):
            diff_consecutivenums(1234)

        with self.assertRaises(TypeError):
            diff_consecutivenums([1, "2", 3, 4])

        with self.assertRaises(TypeError):
            diff_consecutivenums([1, None, 3, 4])
