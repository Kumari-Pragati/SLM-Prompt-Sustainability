import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_positive_integer_input(self):
        """Test parallelogram_perimeter with positive integer inputs"""
        self.assertEqual(parallelogram_perimeter(3, 4), 24)
        self.assertEqual(parallelogram_perimeter(5, 7), 70)

    def test_zero_input(self):
        """Test parallelogram_perimeter with zero input"""
        self.assertEqual(parallelogram_perimeter(0, 5), 0)
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_negative_input(self):
        """Test parallelogram_perimeter with negative input"""
        self.assertEqual(parallelogram_perimeter(-3, 4), 24)
        self.assertRaises(ValueError, lambda: parallelogram_perimeter(-5, -7))

    def test_float_input(self):
        """Test parallelogram_perimeter with float inputs"""
        self.assertAlmostEqual(parallelogram_perimeter(3.5, 4.2), 29.4)
        self.assertAlmostEqual(parallelogram_perimeter(5.0, 7.5), 71.5)
