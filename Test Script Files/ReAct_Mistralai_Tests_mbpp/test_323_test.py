import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(re_arrange([], 0), [])

    def test_single_element(self):
        for num in [-1, 1]:
            self.assertEqual(re_arrange([num], 1), [num])

    def test_two_elements(self):
        for num1, num2 in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
            self.assertEqual(re_arrange([num1, num2], 2), [num2, num1])

    def test_odd_length(self):
        for nums in [(-1, 1, 2), (1, -1, 2), (-1, 1, -2), (1, -1, -2)]:
            self.assertEqual(re_arrange(nums, len(nums)), nums)

    def test_even_length_positive(self):
        for nums in [(1, 2, -1), (2, 1, -1), (2, -1, 1), (-1, 2, 1)]:
            self.assertEqual(re_arrange(nums, len(nums)), nums)

    def test_even_length_negative(self):
        for nums in [(-1, -2, 1), (-2, -1, 1), (-2, 1, -1), (1, -2, -1)]:
            self.assertEqual(re_arrange(nums, len(nums)), nums)

    def test_edge_case_zero(self):
        self.assertEqual(re_arrange([-1], 0), [])
        self.assertEqual(re_arrange([1], 0), [])

    def test_edge_case_length_1(self):
        self.assertEqual(re_arrange([-1], 1), [-1])
        self.assertEqual(re_arrange([1], 1), [1])

    def test_edge_case_length_2(self):
        self.assertEqual(re_arrange([-1, 1], 2), [1, -1])
        self.assertEqual(re_arrange([1, -1], 2), [-1, 1])

    def test_edge_case_length_3(self):
        self.assertEqual(re_arrange([-1, 1, 2], 3), [2, -1, 1])
        self.assertEqual(re_arrange([1, -1, 2], 3), [1, 2, -1])
