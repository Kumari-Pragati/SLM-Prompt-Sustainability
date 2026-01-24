import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_get_item_positive_index(self):
        tup1 = (1, 2, 3, 4, 5)
        self.assertEqual(get_item(tup1, 2), 3)

    def test_get_item_negative_index(self):
        tup1 = (1, 2, 3, 4, 5)
        self.assertEqual(get_item(tup1, -2), 3)

    def test_get_item_out_of_range_index(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, 10)

    def test_get_item_tuple_with_single_element(self):
        tup1 = (1,)
        self.assertEqual(get_item(tup1, 0), 1)

    def test_get_item_tuple_with_empty(self):
        tup1 = ()
        with self.assertRaises(IndexError):
            get_item(tup1, 0)
