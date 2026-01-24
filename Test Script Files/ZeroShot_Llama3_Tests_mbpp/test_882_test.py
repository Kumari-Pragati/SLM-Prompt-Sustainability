import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 60)

    def test_zero_base(self):
        self.assertEqual(parallelogram_perimeter(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_negative_base(self):
        self.assertEqual(parallelogram_perimeter(-5, 10), 60)

    def test_negative_height(self):
        self.assertEqual(parallelogram_perimeter(5, -10), 60)

    def test_zero_base_zero_height(self):
        self.assertEqual(parallelogram_perimeter(0, 0), 0)

    def test_non_zero_base_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_non_zero_base_non_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 60)
