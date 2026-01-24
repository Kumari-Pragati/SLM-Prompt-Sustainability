import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_get_item_typical_case(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 2
        self.assertEqual(get_item(tup1, index), 3)

    def test_get_item_edge_case_empty_tuple(self):
        tup1 = ()
        index = 0
        with self.assertRaises(IndexError):
            get_item(tup1, index)

    def test_get_item_edge_case_negative_index(self):
        tup1 = (1, 2, 3, 4, 5)
        index = -1
        self.assertEqual(get_item(tup1, index), 5)

    def test_get_item_edge_case_out_of_range_index(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 10
        with self.assertRaises(IndexError):
            get_item(tup1, index)

    def test_get_item_error_case_non_integer_index(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 'a'
        with self.assertRaises(TypeError):
            get_item(tup1, index)
