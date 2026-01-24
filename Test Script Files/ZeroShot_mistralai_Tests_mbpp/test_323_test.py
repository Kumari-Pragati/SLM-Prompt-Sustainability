import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_re_arrange_empty_list(self):
        self.assertEqual(re_arrange([], 0), [])

    def test_re_arrange_single_element(self):
        self.assertEqual(re_arrange([1], 0), [1])

    def test_re_arrange_positive_numbers(self):
        self.assertEqual(re_arrange([1, 2, 3, -1, -2, -3], 6), [1, 2, -1, -2, 3, -3])

    def test_re_arrange_negative_numbers(self):
        self.assertEqual(re_arrange([-1, -2, -3, 1, 2, 3], 6), [-1, -2, 1, 2, -3, 3])

    def test_re_arrange_mixed_numbers(self):
        self.assertEqual(re_arrange([1, -1, 2, -2, 3, -3, 4, -4], 8), [1, -1, 2, -2, 3, -3, 4, -4])

    def test_re_arrange_odd_length(self):
        self.assertEqual(re_arrange([1, -1, 2, -2, 3, -3], 6), [1, -1, 2, -2, 3, -3])

    def test_re_arrange_even_length(self):
        self.assertEqual(re_arrange([1, -1, 2, -2, 3, -3, 4, -4], 8), [1, -1, 2, -2, 3, -3, 4, -4])
