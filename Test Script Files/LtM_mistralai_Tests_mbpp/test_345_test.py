import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4]), [1, 1, 1])
        self.assertEqual(diff_consecutivenums([-1, 0, 1]), [-1, 1])
        self.assertEqual(diff_consecutivenums([5, 5, 5]), [0, 0, 0])

    def test_edge_cases(self):
        self.assertEqual(diff_consecutivenums([]), [])
        self.assertEqual(diff_consecutivenums([1]), [0])
        self.assertEqual(diff_consecutivenums([1, 1]), [0])
        self.assertEqual(diff_consecutivenums([2147483647, 0]), [-2147483647])
        self.assertEqual(diff_consecutivenums([0, -2147483648]), [2147483648])

    def test_complex_cases(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5]), [1, 1, 1, 1])
        self.assertEqual(diff_consecutivenums([-1, 0, 1, -2, 3]), [-1, 1, -1, 1])
        self.assertEqual(diff_consecutivenums([5, 5, 5, 4]), [0, 0, -1])
