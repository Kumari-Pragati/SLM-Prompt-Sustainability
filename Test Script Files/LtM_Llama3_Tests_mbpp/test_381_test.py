import unittest
from mbpp_381_code import index_on_inner_list

class TestIndexOnInnerList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(index_on_inner_list([], 0), [])

    def test_single_element_list(self):
        self.assertEqual(index_on_inner_list([[1, 2, 3]], 0), [[1, 2, 3]])

    def test_multiple_elements_list(self):
        self.assertEqual(index_on_inner_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            index_on_inner_list([[1, 2, 3]], 10)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            index_on_inner_list([[1, 2, 3]], -1)

    def test_index_zero(self):
        self.assertEqual(index_on_inner_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_index_one(self):
        self.assertEqual(index_on_inner_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [[1, 2, 3], [2, 5, 6], [7, 8, 9]])

    def test_index_two(self):
        self.assertEqual(index_on_inner_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), [[1, 2, 3], [4, 5, 6], [3, 8, 9]])
