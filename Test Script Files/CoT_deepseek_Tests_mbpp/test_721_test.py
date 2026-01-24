import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_typical_case(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5.0)

    def test_single_element(self):
        cost = [[1]]
        N = 1
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 1.0)

    def test_empty_matrix(self):
        cost = []
        N = 0
        self.assertEqual(maxAverageOfPath(cost, N), 0)

    def test_negative_numbers(self):
        cost = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), -5.0)

    def test_large_numbers(self):
        cost = [[1000, 2000, 3000], [4000, 5000, 6000], [7000, 8000, 9000]]
        N = 3
        self.assertAlmostEqual(maxAverageOfPath(cost, N), 5000.0)

    def test_invalid_input(self):
        cost = "invalid"
        N = 3
        with self.assertRaises(TypeError):
            maxAverageOfPath(cost, N)
