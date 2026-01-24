import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_typical(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 0.5, places=2)

    def test_edge_case(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5]), 0.0, places=2)

    def test_zero(self):
        self.assertAlmostEqual(positive_count([0, 0, 0, 0, 0]), 0.0, places=2)

    def test_all_positive(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1.0, places=2)

    def test_all_negative(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 0.0, places=2)

    def test_mixed(self):
        self.assertAlmostEqual(positive_count([-1, 2, -3, 4, -5]), 0.375, places=2)

    def test_empty(self):
        self.assertEqual(positive_count([]), 0.0)

    def test_single(self):
        self.assertAlmostEqual(positive_count([1]), 1.0, places=2)

    def test_single_negative(self):
        self.assertAlmostEqual(positive_count([-1]), 0.0, places=2)

    def test_single_zero(self):
        self.assertAlmostEqual(positive_count([0]), 0.0, places=2)
