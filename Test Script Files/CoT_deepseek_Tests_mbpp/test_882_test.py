import unittest
from mbpp_882_code import parallelogram_perimeter

class TestParallelogramPerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(parallelogram_perimeter(5, 10), 100)

    def test_zero_input(self):
        self.assertEqual(parallelogram_perimeter(0, 0), 0)

    def test_negative_input(self):
        self.assertEqual(parallelogram_perimeter(-5, -10), 100)

    def test_large_input(self):
        self.assertAlmostEqual(parallelogram_perimeter(10000, 10000), 400000000)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            parallelogram_perimeter("5", 10)
