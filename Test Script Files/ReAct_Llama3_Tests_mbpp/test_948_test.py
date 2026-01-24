import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_typical_case(self):
        tup1 = (1, 2, 3, 4, 5)
        self.assertEqual(get_item(tup1, 2), 3)

    def test_edge_case_index_zero(self):
        tup1 = (1, 2, 3, 4, 5)
        self.assertEqual(get_item(tup1, 0), 1)

    def test_edge_case_index_last(self):
        tup1 = (1, 2, 3, 4, 5)
        self.assertEqual(get_item(tup1, 4), 5)

    def test_edge_case_index_out_of_range(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, 5)

    def test_edge_case_negative_index(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, -1)
