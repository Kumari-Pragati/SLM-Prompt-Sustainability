import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(geometric_sum(3), 1.9375)
        self.assertAlmostEqual(geometric_sum(5), 1.998046875)

    def test_edge_cases(self):
        self.assertEqual(geometric_sum(0), 1)
        self.assertEqual(geometric_sum(-1), 0)

    def test_boundary_cases(self):
        self.assertAlmostEqual(geometric_sum(10), 1.0000000000000004)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            geometric_sum('a')
