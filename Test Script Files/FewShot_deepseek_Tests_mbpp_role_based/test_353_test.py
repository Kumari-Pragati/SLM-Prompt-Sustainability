import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        remove_column(list1, 1)
        self.assertEqual(list1, [[1, 3], [4, 6], [7, 9]])

    def test_edge_condition(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        remove_column(list1, 0)
        self.assertEqual(list1, [[2, 3], [5, 6], [8, 9]])

    def test_boundary_condition(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        remove_column(list1, 2)
        self.assertEqual(list1, [[1, 2], [4, 5], [7, 8]])

    def test_invalid_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            remove_column(list1, 3)
