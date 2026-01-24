import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_edge_case_with_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, 4, 5]), 4)

    def test_edge_case_with_single_positive_number(self):
        self.assertEqual(sum_three_smallest_nums([1]), 0)

    def test_edge_case_with_empty_list(self):
        self.assertEqual(sum_three_smallest_nums([]), 0)

    def test_edge_case_with_all_positive_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3]), 6)

    def test_edge_case_with_all_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3]), 0)

    def test_edge_case_with_duplicates(self):
        self.assertEqual(sum_three_smallest_nums([1, 1, 1, 2, 2, 3]), 3)

    def test_edge_case_with_large_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1000, 2000, 3000, 4000, 5000]), 6000)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sum_three_smallest_nums("not a list")
