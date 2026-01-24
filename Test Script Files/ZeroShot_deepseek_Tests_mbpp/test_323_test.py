import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_re_arrange(self):
        self.assertEqual(re_arrange([1, -2, 3, -4, 5, -6], 6), [1, -2, 3, -4, 5, -6])
        self.assertEqual(re_arrange([1, -2, 3, -4, 5, -6, 7, -8], 8), [1, -2, 3, -4, 5, -6, 7, -8])
        self.assertEqual(re_arrange([-1, -2, 3, 4, 5, -6], 6), [-1, -2, 3, 4, 5, -6])
        self.assertEqual(re_arrange([-1, -2, 3, -4, 5, -6, 7, -8], 8), [-1, -2, 3, -4, 5, -6, 7, -8])
        self.assertEqual(re_arrange([1, 2, 3, 4, 5, 6], 6), [1, 2, 3, 4, 5, 6])
        self.assertEqual(re_arrange([-1, 2, -3, 4, -5, 6], 6), [-1, 2, -3, 4, -5, 6])
