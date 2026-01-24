import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_valid_index(self):
        self.assertEqual(get_item((1, 2, 3), 1), 2)
        self.assertEqual(get_item((4, 5, 6), 2), 5)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), -1)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), 3)

    def test_empty_tuple(self):
        with self.assertRaises(IndexError):
            get_item((), 0)

    def test_non_integer_index(self):
        with self.assertRaises(TypeError):
            get_item((1, 2, 3), 'a')
