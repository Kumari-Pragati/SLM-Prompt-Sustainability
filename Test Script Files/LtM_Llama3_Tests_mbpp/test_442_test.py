import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(positive_count([1, 2, 3, 4, 5]), 1.0)

    def test_simple_negative(self):
        self.assertEqual(positive_count([-1, -2, -3, -4, -5]), 0.0)

    def test_empty_input(self):
        self.assertEqual(positive_count([]), 0.0)

    def test_single_positive(self):
        self.assertEqual(positive_count([1]), 1.0)

    def test_single_negative(self):
        self.assertEqual(positive_count([-1]), 0.0)

    def test_mixed_input(self):
        self.assertAlmostEqual(positive_count([1, -2, 3, -4, 5]), 0.5)

    def test_all_positive(self):
        self.assertEqual(positive_count([1, 2, 3, 4, 5, 6]), 1.0)

    def test_all_negative(self):
        self.assertEqual(positive_count([-1, -2, -3, -4, -5, -6]), 0.0)
