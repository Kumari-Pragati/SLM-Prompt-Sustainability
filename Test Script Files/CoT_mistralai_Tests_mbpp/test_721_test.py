import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):
    def test_typical_case(self):
        cost = [
            [1, 3, 5],
            [2, 6, 7],
            [4, 5, 8]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 5.0)

    def test_edge_case_1(self):
        cost = [
            [1],
            [2]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 1.5)

    def test_edge_case_2(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 5.0)

    def test_edge_case_3(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 6.0)

    def test_invalid_input_1(self):
        with self.assertRaises(ValueError):
            maxAverageOfPath([], 0)

    def test_invalid_input_2(self):
        with self.assertRaises(ValueError):
            maxAverageOfPath([[1]], 0)
