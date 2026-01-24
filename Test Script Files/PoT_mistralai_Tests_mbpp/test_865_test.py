import unittest
from mbpp_865_code import ntimes_list

class TestNtimesList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(ntimes_list([1, 2, 3], 4), [4, 8, 12])

    def test_edge_case_zero(self):
        self.assertEqual(ntimes_list([], 3), [])

    def test_edge_case_one(self):
        self.assertEqual(ntimes_list([1], 0), [])

    def test_edge_case_negative_n(self):
        self.assertEqual(ntimes_list([1, 2, 3], -2), [])

    def test_corner_case_floats(self):
        self.assertListEqual(ntimes_list([1.5, 2.5], 3), [4.5, 7.5])
