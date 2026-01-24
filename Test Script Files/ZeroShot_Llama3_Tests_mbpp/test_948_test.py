import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_get_item_valid_index(self):
        tup1 = (1, 2, 3, 4, 5)
        self.assertEqual(get_item(tup1, 2), 3)

    def test_get_item_invalid_index(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, 10)

    def test_get_item_negative_index(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, -6)

    def test_get_item_index_out_of_range(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, 6)
