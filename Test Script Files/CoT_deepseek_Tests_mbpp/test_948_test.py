import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_get_item_with_valid_tuple_and_index(self):
        self.assertEqual(get_item((1, 2, 3), 1), 2)
        self.assertEqual(get_item(('a', 'b', 'c'), 0), 'a')
        self.assertEqual(get_item((10, 20, 30), 2), 30)

    def test_get_item_with_empty_tuple(self):
        self.assertEqual(get_item((), 0), None)

    def test_get_item_with_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), 5)
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), -4)

    def test_get_item_with_non_tuple_input(self):
        with self.assertRaises(TypeError):
            get_item([1, 2, 3], 1)
        with self.assertRaises(TypeError):
            get_item("abc", 1)
