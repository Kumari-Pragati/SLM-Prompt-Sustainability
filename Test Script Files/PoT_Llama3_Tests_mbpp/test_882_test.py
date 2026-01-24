import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parallelogram_perimeter(5, 3), 30)

    def test_zero_base(self):
        self.assertEqual(parallelogram_perimeter(0, 3), 0)

    def test_zero_height(self):
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_negative_base(self):
        self.assertEqual(parallelogram_perimeter(-5, 3), 30)

    def test_negative_height(self):
        self.assertEqual(parallelogram_perimeter(5, -3), 30)

    def test_non_integer_base(self):
        self.assertEqual(parallelogram_perimeter(5.5, 3), 30)

    def test_non_integer_height(self):
        self.assertEqual(parallelogram_perimeter(5, 3.5), 30)
