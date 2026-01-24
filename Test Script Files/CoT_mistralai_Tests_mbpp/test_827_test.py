import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_column([], 0), 0)

    def test_single_row(self):
        self.assertEqual(sum_column([[1, 2, 3]], 2), 2)

    def test_multiple_rows(self):
        self.assertEqual(sum_column([[1, 2, 3], [4, 5, 6]], 1), 1 + 4)
        self.assertEqual(sum_column([[1, 2, 3], [4, 5, 6]], 2), 2 + 5)
        self.assertEqual(sum_column([[1, 2, 3], [4, 5, 6]], 3), 3 + 6)

    def test_negative_numbers(self):
        self.assertEqual(sum_column([[-1, 2, -3], [4, -5, 6]], 1), -1 + 4)

    def test_invalid_column(self):
        with self.assertRaises(IndexError):
            sum_column([[1, 2, 3], [4, 5, 6]], 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_column('invalid', 0)
        with self.assertRaises(TypeError):
            sum_column([1, 2, 3], 3.5)
