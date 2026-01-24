import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):

    def test_positive_numbers(self):
        """Test parallelogram area with positive base and height."""
        self.assertEqual(parallelogram_area(3, 4), 12)
        self.assertEqual(parallelogram_area(5, 7), 35)

    def test_zero_base(self):
        """Test parallelogram area with zero base."""
        self.assertEqual(parallelogram_area(0, 4), 0)

    def test_zero_height(self):
        """Test parallelogram area with zero height."""
        self.assertEqual(parallelogram_area(3, 0), 0)

    def test_negative_numbers(self):
        """Test parallelogram area with negative base and height."""
        self.assertEqual(parallelogram_area(-3, -4), 12)

    def test_non_numeric_input(self):
        """Test parallelogram area with non-numeric input."""
        self.assertRaises(TypeError, parallelogram_area, 'a', 4)
        self.assertRaises(TypeError, parallelogram_area, 3, 'a')
