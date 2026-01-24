import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertEqual(get_item(('a', 'b', 'c'), 1), 'b')

    def test_negative_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), -1), 'c')

    def test_zero_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), 0), 'a')

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item(('a', 'b', 'c'), 3)

    def test_empty_tuple(self):
        with self.assertRaises(IndexError):
            get_item((), 0)

    def test_large_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), 100), None)
