import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6]), [[1, 4], [2, 5], [3, 6]])

    def test_edge_case_empty_list(self):
        self.assertEqual(zip_list([], [1, 2, 3]), [])
        self.assertEqual(zip_list([1, 2, 3], []), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(zip_list([1], [2, 3]), [[1, 2], [1, 3]])
        self.assertEqual(zip_list([1, 2], [3]), [[1, 3], [2, 3]])

    def test_edge_case_single_element_lists(self):
        self.assertEqual(zip_list([1], [2]), [[1, 2]])
        self.assertEqual(zip_list([1, 2], [2]), [[1, 2]])

    def test_edge_case_lists_of_different_lengths(self):
        self.assertEqual(zip_list([1, 2, 3, 4], [4, 5, 6]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(zip_list([1, 2, 3], [4, 5, 6, 7]), [[1, 4], [2, 5], [3, 6]])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            zip_list(123, [1, 2, 3])
        with self.assertRaises(TypeError):
            zip_list([1, 2, 3], 'abc')
