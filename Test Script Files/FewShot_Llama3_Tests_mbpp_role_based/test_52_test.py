import unittest
from mbpp_52_code import paralleloglogram_area

class TestParallelogramArea(unittest.TestCase):
    def test_positive_base_and_height(self):
        self.assertEqual(parallelogram_area(5, 3), 15)

    def test_zero_base(self):
        self.assertEqual(parallelogram_area(0, 3), 0)

    def test_zero_height(self):
        self.assertEqual(parallelogram_area(5, 0), 0)

    def test_negative_base_and_height(self):
        self.assertEqual(parallelogram_area(-5, -3), 15)

    def test_non_numeric_base(self):
        with self.assertRaises(TypeError):
            parallelogram_area('five', 3)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            parallelogram_area(5, 'three')
