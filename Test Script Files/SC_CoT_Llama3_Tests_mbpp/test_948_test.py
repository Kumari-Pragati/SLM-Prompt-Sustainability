import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_typical_input(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 2
        result = get_item(tup1, index)
        self.assertEqual(result, 3)

    def test_edge_case_index_zero(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 0
        result = get_item(tup1, index)
        self.assertEqual(result, 1)

    def test_edge_case_index_last(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 4
        result = get_item(tup1, index)
        self.assertEqual(result, 5)

    def test_edge_case_index_negative(self):
        tup1 = (1, 2, 3, 4, 5)
        index = -1
        with self.assertRaises(IndexError):
            get_item(tup1, index)

    def test_edge_case_index_out_of_range(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 5
        with self.assertRaises(IndexError):
            get_item(tup1, index)

    def test_edge_case_index_non_integer(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 'a'
        with self.assertRaises(TypeError):
            get_item(tup1, index)
