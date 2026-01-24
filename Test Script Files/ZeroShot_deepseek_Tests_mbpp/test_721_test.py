import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_maxAverageOfPath(self):
        # Test case 1: cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        expected_output = 5.0
        self.assertAlmostEqual(maxAverageOfPath(cost, N), expected_output)

        # Test case 2: cost = [[1, 2], [3, 4]]
        cost = [[1, 2], [3, 4]]
        N = 2
        expected_output = 2.5
        self.assertAlmostEqual(maxAverageOfPath(cost, N), expected_output)

        # Test case 3: cost = [[1]]
        cost = [[1]]
        N = 1
        expected_output = 1.0
        self.assertAlmostEqual(maxAverageOfPath(cost, N), expected_output)

        # Test case 4: cost = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        cost = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        N = 3
        expected_output = 0.0
        self.assertAlmostEqual(maxAverageOfPath(cost, N), expected_output)
