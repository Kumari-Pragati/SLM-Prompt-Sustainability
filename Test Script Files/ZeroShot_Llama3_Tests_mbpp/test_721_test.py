import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_maxAverageOfPath(self):
        cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(maxAverageOfPath(cost, 3), 5.0)
        cost = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(maxAverageOfPath(cost, 4), 6.0)
        cost = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        self.assertEqual(maxAverageOfPath(cost, 5), 6.5)

    def test_maxAverageOfPath_edge_cases(self):
        cost = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(maxAverageOfPath(cost, 2), 3.0)
        cost = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertEqual(maxAverageOfPath(cost, 3), 4.0)
        cost = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        self.assertEqual(maxAverageOfPath(cost, 4), 5.0)
