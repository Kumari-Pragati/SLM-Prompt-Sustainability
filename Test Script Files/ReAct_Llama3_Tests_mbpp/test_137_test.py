import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_zero_count_typical(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, 0, 3, 4, 0]), 0.4, places=2)

    def test_zero_count_edge(self):
        self.assertAlmostEqual(zero_count([0]), 1.0, places=2)

    def test_zero_count_edge2(self):
        self.assertAlmostEqual(zero_count([1]), 0.0, places=2)

    def test_zero_count_edge3(self):
        self.assertAlmostEqual(zero_count([]), 0.0, places=2)

    def test_zero_count_edge4(self):
        self.assertAlmostEqual(zero_count([0, 0, 0]), 1.0, places=2)

    def test_zero_count_edge5(self):
        self.assertAlmostEqual(zero_count([1, 1, 1]), 0.0, places=2)

    def test_zero_count_edge6(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, 3, 4, 5]), 0.3333333333333333, places=2)
