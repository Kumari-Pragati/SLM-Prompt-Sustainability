import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_item(('a', 'b', 'c'), 1), 'b')

    def test_edge_case_first_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), 0), 'a')

    def test_edge_case_last_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), 2), 'c')

    def test_negative_index(self):
        self.assertEqual(get_item(('a', 'b', 'c'), -1), 'c')

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            get_item(('a', 'b', 'c'), 3)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            get_item(['a', 'b', 'c'], 1)

    def test_invalid_input_non_integer_index(self):
        with self.assertRaises(TypeError):
            get_item(('a', 'b', 'c'), '1')
