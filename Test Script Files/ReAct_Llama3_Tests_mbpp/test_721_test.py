import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):
    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertAlmostEqual(maxAverageOfPath(cost, 3) / (2 * 3 - 1), 5.0)

    def test_edge_case_N_1(self):
        cost = [[1]]
        self.assertAlmostEqual(maxAverageOfPath(cost, 1) / (2 * 1 - 1), 1.0)

    def test_edge_case_N_2(self):
        cost = [[1, 2], [3, 4]]
        self.assertAlmostEqual(maxAverageOfPath(cost, 2) / (2 * 2 - 1), 2.5)

    def test_edge_case_M_1(self):
        cost = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]
        self.assertAlmostEqual(maxAverageOfPath(cost, 100) / (2 * 100 - 1), 50.0)

    def test_edge_case_M_N_1(self):
        cost = [[1, 2], [3, 4]]
        self.assertAlmostEqual(maxAverageOfPath(cost, 2) / (2 * 2 - 1), 2.5)

    def test_error_case_invalid_N(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            maxAverageOfPath(cost, 0)

    def test_error_case_invalid_M(self):
        cost = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            maxAverageOfPath(cost, 3)
