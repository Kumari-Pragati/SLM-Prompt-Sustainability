import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4]), [2, 3, 4])
        self.assertListEqual(add_consecutive_nums([5, 6, 7, 8]), [6, 7, 8])

    def test_edge_case_empty_list(self):
        self.assertListEqual(add_consecutive_nums([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(add_consecutive_nums([1]), [])

    def test_edge_case_two_elements(self):
        self.assertListEqual(add_consecutive_nums([1, 2]), [2])

    def test_corner_case_reversed_order(self):
        self.assertListEqual(add_consecutive_nums([4, 3, 2]), [3, 2])
