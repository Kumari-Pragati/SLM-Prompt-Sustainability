import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected = [[1, 3], [4, 6], [7, 9]]
        self.assertEqual(remove_column(list1, n), expected)

    def test_edge_case_empty_list(self):
        list1 = []
        n = 0
        expected = []
        self.assertEqual(remove_column(list1, n), expected)

    def test_boundary_case_single_element(self):
        list1 = [[1]]
        n = 0
        expected = []
        self.assertEqual(remove_column(list1, n), expected)

    def test_invalid_column_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        with self.assertRaises(IndexError):
            remove_column(list1, n)
