import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(ntimes_list([1, 2, 3], 2), [2, 4, 6])
        self.assertEqual(ntimes_list([4, 5, 6], 3), [12, 15, 18])

    def test_edge_cases(self):
        self.assertEqual(ntimes_list([], 3), [])
        self.assertEqual(ntimes_list([0], 3), [0, 0, 0])
        self.assertEqual(ntimes_list([1], 0), [])

    def test_boundary_conditions(self):
        self.assertEqual(ntimes_list([-1, 0, 1], 2), [-2, 0, 2])
        self.assertEqual(ntimes_list([-1, -2, -3], -2), [2, 4, 6])
        self.assertEqual(ntimes_list([1, 2, 3], -2), [-2, -4, -6])
