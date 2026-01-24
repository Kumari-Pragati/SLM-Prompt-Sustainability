import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(parallelogram_perimeter(3, 4), 24)
        self.assertEqual(parallelogram_perimeter(5, 7), 70)
        self.assertEqual(parallelogram_perimeter(10, 15), 300)

    def test_zero_values(self):
        self.assertEqual(parallelogram_perimeter(0, 5), 0)
        self.assertEqual(parallelogram_perimeter(10, 0), 0)

    def test_negative_values(self):
        self.assertEqual(parallelogram_perimeter(-3, 4), 24)
        self.assertRaises(ValueError, lambda: parallelogram_perimeter(-5, -7))

    def test_float_values(self):
        self.assertAlmostEqual(parallelogram_perimeter(3.5, 4.2), 26.2)
        self.assertAlmostEqual(parallelogram_perimeter(5.0, 7.5), 71.5)
