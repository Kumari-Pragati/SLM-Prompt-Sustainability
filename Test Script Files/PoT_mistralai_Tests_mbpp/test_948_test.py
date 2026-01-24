import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_item((1, 2, 3), 1), 2)

    def test_edge_case_empty_tuple(self):
        self.assertIsNone(get_item((), 0))

    def test_edge_case_negative_index(self):
        self.assertIsNone(get_item((1, 2, 3), -1))

    def test_edge_case_out_of_range_index(self):
        self.assertIsNone(get_item((1, 2, 3), 4))
