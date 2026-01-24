import unittest
from mbpp_145_code import max_Abs_Diff

class TestMaxAbsDiff(unittest.TestCase):

    def test_max_Abs_Diff(self):
        self.assertEqual(max_Abs_Diff([1, 3, 9], 3), 8)
        self.assertEqual(max_Abs_Diff([1, 3, 9, 10], 4), 9)
        self.assertEqual(max_Abs_Diff([10, 10, 10], 3), 0)
        self.assertEqual(max_Abs_Diff([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(max_Abs_Diff([-1, -2, -3, -4, -5], 5), 4)
        self.assertEqual(max_Abs_Diff([-1, 2, -3, 4, -5], 5), 6)
