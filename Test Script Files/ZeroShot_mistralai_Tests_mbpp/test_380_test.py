import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(multi_list(0, 0), [])

    def test_single_row(self):
        self.assertEqual(multi_list(1, 1), [[0]])
        self.assertEqual(multi_list(1, 2), [[0], [0 * 1]])
        self.assertEqual(multi_list(1, 3), [[0], [0 * 1], [0 * 1 * 2]])

    def test_single_column(self):
        self.assertEqual(multi_list(2, 1), [[0], [1 * 0], [2 * 1]])
        self.assertEqual(multi_list(3, 1), [[0], [1 * 0], [2 * 1], [3 * 1]])

    def test_multiple_rows_and_columns(self):
        self.assertEqual(multi_list(2, 2), [[0, 0 * 1], [1 * 0, 1 * 1]])
        self.assertEqual(multi_list(3, 3), [[0, 0 * 1, 0 * 1 * 2],
                                             [1 * 0, 1 * 1, 1 * 1 * 2],
                                             [2 * 0, 2 * 1, 2 * 1 * 2]])
