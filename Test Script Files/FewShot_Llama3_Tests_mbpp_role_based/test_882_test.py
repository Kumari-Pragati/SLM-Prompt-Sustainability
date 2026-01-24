import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):
    def test_positive_base_and_height(self):
        self.assertEqual(parallelogram_perimeter(5, 3), 30)

    def test_zero_base(self):
        self.assertEqual(parallelogram_perimeter(0, 3), 0)

    def test_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_negative_base_and_height(self):
        self.assertEqual(parallelogram_perimeter(-5, -3), 30)

    def test_non_numeric_base(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter('five', 3)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter(5, 'three')
