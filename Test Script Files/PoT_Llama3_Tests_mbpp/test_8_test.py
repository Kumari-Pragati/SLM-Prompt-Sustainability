import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])

    def test_edge_case_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(square_nums([5]), [25])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_edge_case_zero(self):
        self.assertEqual(square_nums([0, 0, 0]), [0, 0, 0])

    def test_edge_case_large_numbers(self):
        self.assertEqual(square_nums([100, 200, 300]), [10000, 40000, 90000])

    def test_edge_case_non_integer_numbers(self):
        self.assertEqual(square_nums([1.5, 2.5, 3.5]), [1.5625, 6.25, 12.25])
