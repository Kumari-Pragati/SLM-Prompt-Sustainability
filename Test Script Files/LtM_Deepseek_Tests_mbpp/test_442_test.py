import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(positive_count([1, -2, 3, -4, 5]), 0.4)

    def test_empty_list(self):
        self.assertEqual(positive_count([]), 0.0)

    def test_all_positive(self):
        self.assertEqual(positive_count([1, 2, 3]), 1.0)

    def test_all_negative(self):
        self.assertEqual(positive_count([-1, -2, -3]), 0.0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(positive_count([-1, 2, -3, 4]), 0.5)

    def test_large_numbers(self):
        self.assertAlmostEqual(positive_count([1000, -2000, 3000]), 0.33)

    def test_zero_in_list(self):
        self.assertAlmostEqual(positive_count([0, 1, -2, 3]), 0.5)
