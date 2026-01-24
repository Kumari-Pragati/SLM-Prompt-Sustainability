import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):
    def test_typical_use_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 4.5)

    def test_empty_cost_matrix(self):
        cost = []
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 0)

    def test_single_row_cost_matrix(self):
        cost = [[1]]
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 1)

    def test_single_column_cost_matrix(self):
        cost = [[1]] * M
        self.assertAlmostEqual(maxAverageOfPath(cost, len(cost)), 1)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            maxAverageOfPath(cost, M + 1)
