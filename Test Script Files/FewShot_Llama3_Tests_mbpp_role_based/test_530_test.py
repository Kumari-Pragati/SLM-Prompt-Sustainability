import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(negative_count([]), 0.0)

    def test_all_positive_numbers(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5]), 0.0)

    def test_all_negative_numbers(self):
        self.assertEqual(negative_count([-1, -2, -3, -4, -5]), 1.0)

    def test_mixed_numbers(self):
        self.assertEqual(negative_count([-1, 2, -3, 4, -5]), 0.5)

    def test_single_negative_number(self):
        self.assertEqual(negative_count([1, -2, 3, 4, 5]), 0.2)

    def test_single_positive_number(self):
        self.assertEqual(negative_count([-1, 2, -3, 4, 5]), 0.4)

    def test_list_with_zero(self):
        self.assertEqual(negative_count([0, 1, 2, 3, 4]), 0.0)
