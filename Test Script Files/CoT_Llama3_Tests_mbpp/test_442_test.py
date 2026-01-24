import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_positive_count_typical(self):
        self.assertEqual(positive_count([1, 2, 3, 4, 5]), 3.0)

    def test_positive_count_edge(self):
        self.assertEqual(positive_count([-1, -2, -3, -4, -5]), 0.0)

    def test_positive_count_zero(self):
        self.assertEqual(positive_count([0, 0, 0, 0, 0]), 0.0)

    def test_positive_count_all_positive(self):
        self.assertEqual(positive_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10.0)

    def test_positive_count_all_negative(self):
        self.assertEqual(positive_count([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 0.0)

    def test_positive_count_mixed(self):
        self.assertEqual(positive_count([-1, 2, -3, 4, -5]), 2.0)

    def test_positive_count_empty(self):
        self.assertEqual(positive_count([]), 0.0)

    def test_positive_count_single_negative(self):
        self.assertEqual(positive_count([-1, 2, 3, 4, 5]), 4.0)

    def test_positive_count_single_zero(self):
        self.assertEqual(positive_count([0, 1, 2, 3, 4]), 4.0)
