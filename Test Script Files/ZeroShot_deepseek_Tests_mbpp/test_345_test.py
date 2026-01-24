import unittest
from mbpp_345_code import diff_consecutivenums

class TestDiffConsecutiveNums(unittest.TestCase):

    def test_diff_consecutivenums(self):
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4]), [1, 1])
        self.assertEqual(diff_consecutivenums([5, 10, 15]), [5, 5])
        self.assertEqual(diff_consecutivenums([10, 20, 30, 40, 50]), [10, 10, 10, 10])
        self.assertEqual(diff_consecutivenums([1, 2, 3, 4, 5, 6]), [1, 1, 1, 1])
        self.assertEqual(diff_consecutivenums([100, 80, 60, 40]), [20, 20])
