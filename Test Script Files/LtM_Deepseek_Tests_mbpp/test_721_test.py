import unittest
from mbpp_721_code import maxAverageOfPath

class TestMaxAverageOfPath(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(maxAverageOfPath([[1, 2], [3, 4]], 2), 2.5)

    def test_edge_conditions(self):
        self.assertEqual(maxAverageOfPath([[1]], 1), 1)
        self.assertEqual(maxAverageOfPath([], 0), 0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 5.0)

    def test_complex_cases(self):
        self.assertAlmostEqual(maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 5.0)
        self.assertAlmostEqual(maxAverageOfPath([[1, 2], [3, 4]], 2), 2.5)
