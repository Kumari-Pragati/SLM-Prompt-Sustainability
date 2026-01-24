import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(multi_list(2, 2), [[0, 0], [0, 0]])

    def test_edge_row(self):
        self.assertEqual(multi_list(1, 2), [[0, 0]])

    def test_edge_col(self):
        self.assertEqual(multi_list(2, 1), [[0], [0]])

    def test_edge_zero(self):
        self.assertEqual(multi_list(0, 0), [])

    def test_edge_negative(self):
        with self.assertRaises(ValueError):
            multi_list(-1, 2)

    def test_edge_non_integer(self):
        with self.assertRaises(TypeError):
            multi_list('a', 2)

    def test_edge_non_positive(self):
        with self.assertRaises(ValueError):
            multi_list(2, -1)
