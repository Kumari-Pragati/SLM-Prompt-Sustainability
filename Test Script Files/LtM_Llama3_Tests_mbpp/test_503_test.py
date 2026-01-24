import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_single_element_input(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_two_elements_input(self):
        self.assertEqual(add_consecutive_nums([1, 2]), [1])

    def test_three_elements_input(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3]), [1, 1])

    def test_negative_numbers_input(self):
        self.assertEqual(add_consecutive_nums([-1, -2, -3]), [-1, -1])

    def test_positive_numbers_input(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 1, 1])

    def test_mixed_numbers_input(self):
        self.assertEqual(add_consecutive_nums([-1, 0, 1]), [-1, 1])

    def test_large_numbers_input(self):
        self.assertEqual(add_consecutive_nums([100, 200, 300]), [100, 100])

    def test_edge_case_input(self):
        self.assertEqual(add_consecutive_nums([1, 1]), [0])
