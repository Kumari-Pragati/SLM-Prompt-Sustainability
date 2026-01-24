import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multi_list(3, 3), [[0, 0, 0], [0, 1, 2], [0, 2, 4]])

    def test_single_row(self):
        self.assertEqual(multi_list(1, 3), [[0, 0, 0]])

    def test_single_column(self):
        self.assertEqual(multi_list(3, 1), [[0], [0], [0]])

    def test_zero_rows(self):
        self.assertEqual(multi_list(0, 3), [])

    def test_zero_columns(self):
        self.assertEqual(multi_list(3, 0), [[] for _ in range(3)])

    def test_negative_rows(self):
        with self.assertRaises(AssertionError):
            multi_list(-3, 3)

    def test_negative_columns(self):
        with self.assertRaises(AssertionError):
            multi_list(3, -3)

    def test_non_integer_rows(self):
        with self.assertRaises(TypeError):
            multi_list(3.5, 3)

    def test_non_integer_columns(self):
        with self.assertRaises(TypeError):
            multi_list(3, 3.5)
