import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_edge_case_empty_list(self):
        self.assertEqual(sub_list([1, 2, 3], []), [1, 2, 3])

    def test_edge_case_single_element_list(self):
        self.assertEqual(sub_list([1], [2]), [-1])

    def test_edge_case_empty_lists(self):
        self.assertEqual(sub_list([], []), [])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(sub_list([1], [1]), [])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sub_list([-1, 2, 3], [4, 5, 6]), [-5, 1, -3])

    def test_edge_case_large_numbers(self):
        self.assertEqual(sub_list([100, 200, 300], [400, 500, 600]), [-300, -300, -300])
