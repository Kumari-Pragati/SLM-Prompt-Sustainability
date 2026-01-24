import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertAlmostEqual(positive_count([]), 0.00)

    def test_all_positive(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4, 5]), 1.00)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(positive_count([1, -2, 3, -4, 5]), 3/5)

    def test_zero(self):
        self.assertAlmostEqual(positive_count([0, 1, -2, 3, -4, 5]), 3/6)

    def test_negative_list(self):
        self.assertAlmostEqual(positive_count([-1, -2, -3, -4, -5]), 0.00)

    def test_float_numbers(self):
        self.assertAlmostEqual(positive_count([1.1, -2.2, 3.3, -4.4, 5.5]), 1.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            positive_count('string')
