import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_edge_case_zero(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [])

    def test_edge_case_negative(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 2), [-2, -4, -6])

    def test_edge_case_single_element(self):
        self.assertEqual(ntimes_list([5], 3), [15])

    def test_edge_case_empty_list(self):
        self.assertEqual(ntimes_list([], 2), [])

    def test_edge_case_single_element_zero(self):
        self.assertEqual(ntimes_list([0], 2), [0])

    def test_edge_case_single_element_negative(self):
        self.assertEqual(ntimes_list([-5], 2), [-10])

    def test_edge_case_list_of_zeros(self):
        self.assertEqual(ntimes_list([0, 0, 0], 2), [0, 0, 0])

    def test_edge_case_list_of_negatives(self):
        self.assertEqual(ntimes_list([-5, -2, -1], 2), [-10, -4, -2])
