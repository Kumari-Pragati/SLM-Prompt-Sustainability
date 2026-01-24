import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_positive_integer_list(self):
        self.assertEqual(sum_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 21)
        self.assertEqual(sum_column([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 2), 1600)

    def test_empty_list(self):
        self.assertEqual(sum_column([], 0), 0)

    def test_negative_integer_list(self):
        self.assertEqual(sum_column([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], 1), -21)

    def test_mixed_integer_list(self):
        self.assertEqual(sum_column([[1, -2, 3], [4, 5, -6], [7, -8, 9]], 1), 12)

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            sum_column([[1, 'a', 3], [4, 'b', 6], [7, 'c', 9]], 1)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            sum_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1)

    def test_out_of_range_index(self):
        with self.assertRaises(IndexError):
            sum_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)
