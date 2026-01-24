import unittest
from mbpp_865_code import ntimes_list

class TestNTimesList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(ntimes_list([], 3), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(ntimes_list([5], 7), [35])

    def test_boundary_case_large_numbers(self):
        self.assertEqual(ntimes_list([1000000000, 2000000000], 2), [2000000000, 4000000000])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(ntimes_list([-1, -2, -3], 3), [-3, -6, -9])

    def test_corner_case_zero_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], 0), [0, 0, 0])

    def test_corner_case_large_multiplier(self):
        self.assertEqual(ntimes_list([1, 2, 3], 1000000), [1000000, 2000000, 3000000])
