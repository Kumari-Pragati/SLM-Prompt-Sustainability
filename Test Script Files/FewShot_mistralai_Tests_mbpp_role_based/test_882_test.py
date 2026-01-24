import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):
    def test_positive_b_and_h(self):
        self.assertEqual(parallelogram_perimeter(3, 4), 24)

    def test_zero_b_and_h(self):
        self.assertEqual(parallelogram_perimeter(0, 0), 0)

    def test_negative_b_and_h(self):
        self.assertEqual(parallelogram_perimeter(-3, -4), 24)

    def test_zero_and_positive_h(self):
        self.assertEqual(parallelogram_perimeter(0, 4), 16)

    def test_positive_and_zero_h(self):
        self.assertEqual(parallelogram_perimeter(3, 0), 0)
