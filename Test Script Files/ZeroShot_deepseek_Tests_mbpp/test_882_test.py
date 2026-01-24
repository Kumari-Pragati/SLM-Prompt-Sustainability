import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(parallelogram_perimeter(2, 3), 12)
        self.assertEqual(parallelogram_perimeter(5, 4), 40)
        self.assertEqual(parallelogram_perimeter(10, 2), 40)

    def test_negative_values(self):
        self.assertEqual(parallelogram_perimeter(-2, 3), -12)
        self.assertEqual(parallelogram_perimeter(-5, 4), -20)
        self.assertEqual(parallelogram_perimeter(-10, 2), -20)

    def test_zero_values(self):
        self.assertEqual(parallelogram_perimeter(0, 3), 0)
        self.assertEqual(parallelogram_perimeter(5, 0), 0)
        self.assertEqual(parallelogram_perimeter(0, 0), 0)

    def test_non_integer_values(self):
        self.assertEqual(parallelogram_perimeter(2.5, 3), 15)
        self.assertEqual(parallelogram_perimeter(5, 4.5), 22.5)
        self.assertEqual(parallelogram_perimeter(10.5, 2), 21)
