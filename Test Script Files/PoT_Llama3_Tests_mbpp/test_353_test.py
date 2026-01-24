import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):
    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        expected = [[1, 3], [4, 6], [7, 9]]
        self.assertEqual(remove_column(list1, n), expected)

    def test_edge_case(self):
        list1 = [[1, 2, 3], [4, 5, 6]]
        n = 0
        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(remove_column(list1, n), expected)

    def test_edge_case2(self):
        list1 = [[1, 2, 3]]
        n = 0
        expected = [[1, 2, 3]]
        self.assertEqual(remove_column(list1, n), expected)

    def test_edge_case3(self):
        list1 = [[1, 2, 3]]
        n = 2
        expected = [[1, 2]]
        self.assertEqual(remove_column(list1, n), expected)

    def test_edge_case4(self):
        list1 = [[1, 2, 3]]
        n = 3
        expected = [[1, 2, 3]]
        self.assertEqual(remove_column(list1, n), expected)

    def test_invalid_input(self):
        list1 = [[1, 2, 3], [4, 5, 6]]
        n = 4
        with self.assertRaises(IndexError):
            remove_column(list1, n)
