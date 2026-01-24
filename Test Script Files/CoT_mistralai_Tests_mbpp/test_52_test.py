import unittest
from mbpp_52_code import parallelogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(parallelogram_area(3, 4), 12)
        self.assertEqual(parallelogram_area(5, 7), 35)

    def test_zero_values(self):
        self.assertEqual(parallelogram_area(0, 5), 0)
        self.assertEqual(parallelogram_area(5, 0), 0)

    def test_negative_values(self):
        self.assertEqual(parallelogram_area(-3, 4), -12)
        self.assertEqual(parallelogram_area(3, -4), -12)

    def test_float_values(self):
        self.assertAlmostEqual(parallelogram_area(3.5, 4.2), 14.7)
        self.assertAlmostEqual(parallelogram_area(5.7, 7.3), 40.81)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, parallelogram_area, 'a', 5)
        self.assertRaises(TypeError, parallelogram_area, 5, 'b')
