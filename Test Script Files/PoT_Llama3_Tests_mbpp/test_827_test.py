import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 12)

    def test_edge_case(self):
        list1 = [[1, 2, 3], [4, 5, 6]]
        C = 2
        self.assertEqual(sum_column(list1, C), 9)

    def test_edge_case2(self):
        list1 = [[1, 2, 3]]
        C = 0
        self.assertEqual(sum_column(list1, C), 1)

    def test_edge_case3(self):
        list1 = [[1, 2, 3]]
        C = 3
        self.assertEqual(sum_column(list1, C), 1)

    def test_invalid_input(self):
        list1 = [[1, 2, 3]]
        C = 4
        with self.assertRaises(IndexError):
            sum_column(list1, C)

    def test_empty_list(self):
        list1 = []
        C = 0
        self.assertEqual(sum_column(list1, C), 0)

    def test_single_element_list(self):
        list1 = [[1, 2, 3]]
        C = 1
        self.assertEqual(sum_column(list1, C), 2)
