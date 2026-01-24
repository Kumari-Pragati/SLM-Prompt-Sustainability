import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_geometric_sum(self):
        self.assertAlmostEqual(geometric_sum(0), 1.0)
        self.assertAlmostEqual(geometric_sum(1), 1.5)
        self.assertAlmostEqual(geometric_sum(2), 1.75)
        self.assertAlmostEqual(geometric_sum(3), 1.875)
        self.assertAlmostEqual(geometric_sum(4), 1.9375)
        self.assertAlmostEqual(geometric_sum(-1), 0)
