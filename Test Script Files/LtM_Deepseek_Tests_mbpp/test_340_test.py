import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_typical_input(self):
        self.assertEqual(sum_three_smallest_nums([10, 20, 30, 40, 50]), 60)

    def test_edge_condition_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(sum_three_smallest_nums([1]), 0)

    def test_edge_condition_two_elements(self):
        self.assertEqual(sum_three_smallest_nums([1, 2]), 0)

    def test_edge_condition_all_positive(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3]), 6)

    def test_edge_condition_all_negative(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), 0)

    def test_edge_condition_all_zero(self):
        self.assertEqual(sum_three_smallest_nums([0, 0, 0]), 0)

    def test_complex_input(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, -4, -5, -6]), 6)
