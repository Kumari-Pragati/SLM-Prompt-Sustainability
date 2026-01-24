import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_get_item_valid_index(self):
        test_tuple = (1, 2, 3, 4, 5)
        result = get_item(test_tuple, 2)
        self.assertEqual(result, 3)

    def test_get_item_invalid_index(self):
        test_tuple = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(test_tuple, -1)

    def test_get_item_empty_tuple(self):
        test_tuple = ()
        with self.assertRaises(IndexError):
            get_item(test_tuple, 0)
