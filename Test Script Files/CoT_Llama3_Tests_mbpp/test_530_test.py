import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(negative_count([1, 2, 3, 4, 5]), 0.0)

    def test_negative_numbers(self):
        self.assertEqual(negative_count([-1, -2, -3, -4, -5]), 1.0)

    def test_mixed_numbers(self):
        self.assertEqual(negative_count([-1, 2, -3, 4, -5]), 0.4)

    def test_empty_list(self):
        self.assertEqual(negative_count([]), 0.0)

    def test_single_number(self):
        self.assertEqual(negative_count([1]), 0.0)

    def test_single_negative_number(self):
        self.assertEqual(negative_count([-1]), 1.0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            negative_count([1, 2, '3', 4, 5])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            negative_count(123)
