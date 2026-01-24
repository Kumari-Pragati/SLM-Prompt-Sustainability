import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_positive_count_typical(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 0.5, places=2)

    def test_positive_count_edge(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, 4, 5]), 0.5, places=2)

    def test_positive_count_zero(self):
        self.assertAlmostEqual(positive_count([0, 0, 0]), 0.0, places=2)

    def test_positive_count_all_negative(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5]), 0.0, places=2)

    def test_positive_count_all_positive(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 1.0, places=2)

    def test_positive_count_mixed(self):
        self.assertAlmostEqual(positive_count([-1, 0, 1, 2, 3]), 0.4, places=2)
