import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(get_item((1, 2, 3), 0), 1)
        self.assertEqual(get_item((1, 2, 3), 1), 2)
        self.assertEqual(get_item((1, 2, 3), 2), 3)

    def test_edge_case_index_out_of_range(self):
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), 3)

    def test_edge_case_negative_index(self):
        with self.assertRaises(IndexError):
            get_item((1, 2, 3), -1)

    def test_edge_case_index_zero(self):
        self.assertEqual(get_item((1, 2, 3), 0), 1)

    def test_edge_case_index_last(self):
        self.assertEqual(get_item((1, 2, 3), 2), 3)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            get_item(123, 0)

    def test_invalid_input_non_integer_index(self):
        with self.assertRaises(TypeError):
            get_item((1, 2, 3), 'a')
