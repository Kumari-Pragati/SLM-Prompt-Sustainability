import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_simple(self):
        self.assertAlmostEqual(zero_count([0, 0, 1, 2, 3]), 0.6)
        self.assertAlmostEqual(zero_count([1, 2, 3, 4, 5]), 0)
        self.assertAlmostEqual(zero_count([0, 0, 0]), 1.0)

    def test_edge_and_boundary(self):
        self.assertAlmostEqual(zero_count([0] * 1000001), 1.0)
        self.assertAlmostEqual(zero_count([-1, 0, 1]), 0.33333333333333337)
        self.assertAlmostEqual(zero_count([0] * 100 + [1]), 0.9999999999999999)

    def test_complex(self):
        self.assertAlmostEqual(zero_count(list(range(10)) + [0] + list(range(10, 20))), 0.5)
        self.assertAlmostEqual(zero_count(list(range(100)) + [0] * 1000 + list(range(2000, 3000))), 0.005)
