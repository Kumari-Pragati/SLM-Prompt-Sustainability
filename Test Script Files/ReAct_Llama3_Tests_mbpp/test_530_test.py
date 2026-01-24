import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(negative_count([-1, -2, -3, -4, -5]), 1.0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(negative_count([-1, 2, -3, 4, -5]), 0.4)

    def test_empty_list(self):
        self.assertEqual(negative_count([]), 0)

    def test_single_negative_number(self):
        self.assertAlmostEqual(negative_count([-1]), 1.0)

    def test_single_positive_number(self):
        self.assertEqual(negative_count([1]), 0)

    def test_all_negative_numbers(self):
        self.assertAlmostEqual(negative_count([-1, -2, -3, -4, -5, -6]), 1.0)

    def test_all_positive_numbers(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5, 6]), 0)

    def test_no_numbers(self):
        with self.assertRaises(TypeError):
            negative_count("")
