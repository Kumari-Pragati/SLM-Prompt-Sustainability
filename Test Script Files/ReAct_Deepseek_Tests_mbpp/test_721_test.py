import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        expected_result = 5.0
        self.assertAlmostEqual(maxAverageOfPath(cost, N), expected_result)

    def test_edge_case_single_element(self):
        cost = [[1]]
        N = 1
        expected_result = 1.0
        self.assertAlmostEqual(maxAverageOfPath(cost, N), expected_result)

    def test_edge_case_empty_matrix(self):
        cost = []
        N = 0
        expected_result = 0.0
        self.assertAlmostEqual(maxAverageOfPath(cost, N), expected_result)

    def test_error_case_invalid_input(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
        N = 3
        with self.assertRaises(TypeError):
            maxAverageOfPath(cost, N)
