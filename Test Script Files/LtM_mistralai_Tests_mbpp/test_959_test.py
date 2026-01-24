import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(Average([1, 2, 3]), 2)
        self.assertEqual(Average([4, 4, 4]), 4)
        self.assertEqual(Average([0, 0, 0]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Average([]), 0)
        self.assertEqual(Average([float('inf')]), float('inf'))
        self.assertEqual(Average([float('-inf')]), float('-inf'))

    def test_complex_input(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5]), -3)
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertAlmostEqual(Average([-1, -2, -3, -4, -5, -6]), -3.5)
