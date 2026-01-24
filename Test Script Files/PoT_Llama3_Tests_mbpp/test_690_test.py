import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2, 6, 12])

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2]), [])

    def test_edge_case_three_element_list(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3]), [2])

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 2, 3, 3, 3]), [2, 6, 9])

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([-1, 2, 3, -4, 5]), [-2, 6, -20])

    def test_edge_case_list_with_mixed_positive_and_negative_numbers(self):
        self.assertEqual(mul_consecutive_nums([1, -2, 3, -4, 5]), [-2, 12, -20])
