import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_single_list(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        result = extract_column(list1, n)
        self.assertEqual(result, [3, 6, 9])

    def test_multiple_lists(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        list2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
        n = 2
        result = extract_column([list1, list2], n)
        self.assertEqual(result, [3, 6, 9, 12, 15, 18])

    def test_invalid_n(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 4
        with self.assertRaises(IndexError):
            extract_column(list1, n)

    def test_empty_list(self):
        list1 = []
        n = 1
        result = extract_column(list1, n)
        self.assertEqual(result, [])
