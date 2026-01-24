import unittest
from mbpp_340_code import sum_three_smallest_nums

class TestSumThreeSmallestNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3, 4, 5]), 6)

    def test_edge_case_with_negative_numbers(self):
        self.assertEqual(sum_three_smallest_nums([-1, -2, -3, 4, 5]), 4)

    def test_boundary_case_with_same_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 1, 1, 1, 1]), 3)

    def test_boundary_case_with_small_numbers(self):
        self.assertEqual(sum_three_smallest_nums([1, 2, 3]), 6)

    def test_invalid_input_with_empty_list(self):
        with self.assertRaises(TypeError):
            sum_three_smallest_nums([])

    def test_invalid_input_with_non_list_input(self):
        with self.assertRaises(TypeError):
            sum_three_smallest_nums("1,2,3")

    def test_invalid_input_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            sum_three_smallest_nums([1, "2", 3])
