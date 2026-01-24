import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_parallelogram_perimeter_positive(self):
        self.assertEqual(parallelogram_perimeter(3, 4), 24)
        self.assertEqual(parallelogram_perimeter(5, 7), 70)
        self.assertEqual(parallelogram_perimeter(10, 12), 240)

    def test_parallelogram_perimeter_zero(self):
        self.assertEqual(parallelogram_perimeter(0, 4), 0)
        self.assertEqual(parallelogram_perimeter(3, 0), 0)

    def test_parallelogram_perimeter_negative(self):
        self.assertEqual(parallelogram_perimeter(-3, 4), 24)
        self.assertEqual(parallelogram_perimeter(3, -4), 24)
