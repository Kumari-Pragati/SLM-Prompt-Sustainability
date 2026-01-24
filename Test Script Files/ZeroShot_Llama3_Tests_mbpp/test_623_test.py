import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_nth_nums(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 2), [1, 4, 9, 16, 25])
        self.assertEqual(nth_nums([-1, -2, -3, -4, -5], 2), [1, 4, 9, 16, 25])
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 3), [1, 8, 27, 64, 125])
        self.assertEqual(nth_nums([-1, -2, -3, -4, -5], 3), [1, 8, 27, 64, 125])
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 4), [1, 16, 81, 256, 625])
        self.assertEqual(nth_nums([-1, -2, -3, -4, -5], 4), [1, 16, 81, 256, 625])
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 5), [1, 32, 243, 1024, 3125])
        self.assertEqual(nth_nums([-1, -2, -3, -4, -5], 5), [1, 32, 243, 1024, 3125])
