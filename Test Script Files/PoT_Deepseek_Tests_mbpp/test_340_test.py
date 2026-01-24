import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_three_smallest_nums([1]), 0)

    def test_two_elements(self):
        self.assertEqual(sum_three_smallest_nums([2, 1]), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), 0)

    def test_duplicates(self):
        self.assertEqual(sum_three_smallest_nums([1, 1, 1]), 1)

    def test_large_numbers(self):
        self.assertEqual(sum_three_smallest_nums([100, 200, 300, 400, 500]), 600)

    def test_mixed_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, 1, 0]), 0)
