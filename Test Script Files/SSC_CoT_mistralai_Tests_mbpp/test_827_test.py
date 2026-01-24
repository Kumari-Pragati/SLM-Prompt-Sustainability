import unittest
from mbpp_827_code import sum_column

class TestSumColumn(unittest.TestCase):

    def test_normal_input(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(sum_column(data, 1), 6)
        self.assertEqual(sum_column(data, 2), 15)
        self.assertEqual(sum_column(data, 3), 24)

    def test_edge_and_boundary_conditions(self):
        data = [
            [0, 0, 0],
            [1, 1, 1],
            [2, 2, 2]
        ]
        self.assertEqual(sum_column(data, 0), 0)
        self.assertEqual(sum_column(data, 1), 3)
        self.assertEqual(sum_column(data, 2), 6)

        data = [
            [1000000000, 2, 3],
            [4, 500000000, 6],
            [7, 8, 900000000]
        ]
        self.assertEqual(sum_column(data, 1), 13)
        self.assertEqual(sum_column(data, 2), 28)
        self.assertEqual(sum_column(data, 3), 66)

    def test_negative_numbers(self):
        data = [
            [-1, 2, 3],
            [-4, 5, -6],
            [-7, 8, 9]
        ]
        self.assertEqual(sum_column(data, 1), -3)
        self.assertEqual(sum_column(data, 2), 17)
        self.assertEqual(sum_column(data, 3), 26)

    def test_empty_list(self):
        self.assertIsNone(sum_column([], 1))

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            sum_column([[1, 2, 3]], 4)
