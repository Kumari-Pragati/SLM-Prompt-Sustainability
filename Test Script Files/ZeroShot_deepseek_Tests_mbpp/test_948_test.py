import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_get_item_with_valid_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), 1), 'b')

    def test_get_item_with_negative_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), -1), 'c')

    def test_get_item_with_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item(('a', 'b', 'c'), 5)

    def test_get_item_with_negative_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item(('a', 'b', 'c'), -5)
