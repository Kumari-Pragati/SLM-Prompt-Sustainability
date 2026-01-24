import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(multi_list(2, 3), [[0, 0, 0], [2, 3, 4]])
        self.assertEqual(multi_list(3, 4), [[0, 0, 0, 0], [0, 3, 6, 9], [0, 4, 8, 12]])

    def test_edge_conditions(self):
        self.assertEqual(multi_list(0, 3), [])
        self.assertEqual(multi_list(1, 0), [[]])
        self.assertEqual(multi_list(1, 1), [[0]])

    def test_boundary_conditions(self):
        self.assertEqual(multi_list(1, 100), [[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]])
        self.assertEqual(multi_list(100, 1), [0] * 100)
