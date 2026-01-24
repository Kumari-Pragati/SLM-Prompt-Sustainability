import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_simple_positive(self):
        self.assertAlmostEqual(positive_count([1, 2, 3]), 1.0)

    def test_simple_zero(self):
        self.assertAlmostEqual(positive_count([0, 0, 0]), 0.0)

    def test_simple_negative(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3]), 0.0)

    def test_edge_case_empty(self):
        self.assertAlmostEqual(positive_count([]), 0.0)

    def test_edge_case_single_zero(self):
        self.assertAlmostEqual(positive_count([0]), 0.0)

    def test_edge_case_single_positive(self):
        self.assertAlmostEqual(positive_count([1]), 1.0)

    def test_edge_case_single_negative(self):
        self.assertAlmostEqual(positive_count([-1]), 0.0)

    def test_edge_case_min_max_values(self):
        self.assertAlmostEqual(positive_count(range(sys.maxsize)), 1.0)
        self.assertAlmostEqual(positive_count(range(-sys.maxsize, 0)), 0.0)
