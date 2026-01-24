import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_typical_input(self):
        cost = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(maxAverageOfPath(cost, len(cost)), 5.0)

    def test_edge_cases(self):
        self.assertEqual(maxAverageOfPath([[1]], 1), 1.0)
        self.assertEqual(maxAverageOfPath([[1, 2], [3, 4]], 2), 2.5)
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 5.0)
        self.assertEqual(maxAverageOfPath([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 4), 7.5)

    def test_boundary_conditions(self):
        self.assertEqual(maxAverageOfPath([[1]], 0), 1.0)
        self.assertEqual(maxAverageOfPath([[1, 2], [3, 4]], 3), 2.5)
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), 1.0)
        self.assertEqual(maxAverageOfPath([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 5), 9.5)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            maxAverageOfPath([[1]], -1)
        with self.assertRaises(IndexError):
            maxAverageOfPath([[1, 2]], 3)
        with self.assertRaises(IndexError):
            maxAverageOfPath([[1, 2, 3]], 0)
        with self.assertRaises(IndexError):
            maxAverageOfPath([[1, 2, 3]], 4)
