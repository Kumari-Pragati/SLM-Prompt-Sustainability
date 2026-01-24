import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 60)

    def test_zero_base(self):
        self.assertEqual(parallelogram_perimeter(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_negative_base(self):
        self.assertEqual(parallelogram_perimeter(-5, 10), 0)

    def test_negative_height(self):
        self.assertEqual(parallelogram_perimeter(5, -10), 0)

    def test_zero_base_and_height(self):
        self.assertEqual(parallelogram_perimeter(0, 0), 0)

    def test_nonzero_base_and_height(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 60)
