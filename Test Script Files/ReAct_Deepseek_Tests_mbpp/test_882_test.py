import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parallelogram_perimeter(5, 10), 100)

    def test_zero_base_or_height(self):
        self.assertEqual(parallelogram_perimeter(0, 10), 0)
        self.assertEqual(parallelogram_perimeter(5, 0), 0)

    def test_negative_base_or_height(self):
        self.assertEqual(parallelogram_perimeter(-5, 10), 0)
        self.assertEqual(parallelogram_perimeter(5, -10), 0)
        self.assertEqual(parallelogram_perimeter(-5, -10), 0)

    def test_large_numbers(self):
        self.assertEqual(parallelogram_perimeter(10000, 20000), 600000000)
