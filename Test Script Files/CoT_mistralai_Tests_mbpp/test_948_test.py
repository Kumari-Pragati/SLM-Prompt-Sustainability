import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_get_item_valid_index(self):
        tup1 = (1, 2, 3, 4, 5)
        self.assertEqual(get_item(tup1, 0), 1)
        self.assertEqual(get_item(tup1, 4), 5)

    def test_get_item_negative_index(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, -1)
        with self.assertRaises(IndexError):
            get_item(tup1, -5)

    def test_get_item_out_of_range_index(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(tup1, 6)
        with self.assertRaises(IndexError):
            get_item(tup1, len(tup1) + 1)

    def test_get_item_non_integer_index(self):
        tup1 = (1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            get_item(tup1, 'a')
        with self.assertRaises(TypeError):
            get_item(tup1, 3.14)
