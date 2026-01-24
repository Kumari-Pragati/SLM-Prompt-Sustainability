import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(negative_count([1, -2, 3, -4, 5, -6]), 0.33, 2)

    def test_empty_list(self):
        self.assertEqual(negative_count([]), 0.0)

    def test_all_positive(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5]), 0.0)

    def test_all_negative(self):
        self.assertEqual(negative_count([-1, -2, -3, -4, -5]), 1.0)

    def test_all_zero(self):
        self.assertEqual(negative_count([0, 0, 0, 0, 0]), 0.0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(negative_count([-1, 0, 1, -2, 2]), 0.33, 2)

    def test_large_numbers(self):
        self.assertAlmostEqual(negative_count(list(range(-1000, 1000, 2))), 0.5, 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            negative_count("not a list")

        with self.assertRaises(TypeError):
            negative_count(123)

        with self.assertRaises(TypeError):
            negative_count(None)
