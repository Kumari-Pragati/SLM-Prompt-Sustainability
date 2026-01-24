import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_item((1, 2, 3), 1), 2)

    def test_edge_case_zero_index(self):
        self.assertEqual(get_item((1, 2, 3), 0), 1)

    def test_boundary_case_last_index(self):
        self.assertEqual(get_item((1, 2, 3), 2), 3)

    def test_negative_index(self):
        self.assertEqual(get_item((1, 2, 3), -1), 3)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), 3)

    def test_negative_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), -4)
