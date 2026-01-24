import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_item((1, 2, 3), 1), 2)

    def test_edge_cases(self):
        self.assertEqual(get_item((1, 2, 3), 0), 1)
        self.assertEqual(get_item((1, 2, 3), 2), 3)
        self.assertEqual(get_item((), 0), None)
        self.assertEqual(get_item((1,), 0), 1)
        self.assertEqual(get_item((1, 2, 3, 4), 4), 4)

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: get_item((1, 2, 3), -1))

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, lambda: get_item((1, 2, 3), 5))
