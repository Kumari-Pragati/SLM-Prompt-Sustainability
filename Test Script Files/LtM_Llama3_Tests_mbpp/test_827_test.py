import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_simple(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 12)

    def test_empty_list(self):
        list1 = []
        C = 1
        self.assertEqual(sum_column(list1, C), 0)

    def test_non_integer_values(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 1
        self.assertEqual(sum_column(list1, C), 12)

    def test_invalid_input_type(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 'a'
        with self.assertRaises(TypeError):
            sum_column(list1, C)

    def test_invalid_input_value(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 10
        self.assertEqual(sum_column(list1, C), 0)

    def test_single_element_list(self):
        list1 = [[1, 2, 3]]
        C = 1
        self.assertEqual(sum_column(list1, C), 3)

    def test_single_element_row(self):
        list1 = [[1, 2, 3]]
        C = 0
        self.assertEqual(sum_column(list1, C), 1)

    def test_zeroth_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = 0
        self.assertEqual(sum_column(list1, C), 1 + 4 + 7)

    def test_negative_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        C = -1
        with self.assertRaises(IndexError):
            sum_column(list1, C)
