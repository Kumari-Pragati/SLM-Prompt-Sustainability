import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(perimeter(5, 3), 18)
        self.assertEqual(perimeter(10, 2), 26)

    def test_zero_values(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)

    def test_negative_values(self):
        self.assertEqual(perimeter(-3, 2), 8)
        self.assertEqual(perimeter(2, -3), 8)

    def test_one_zero_value(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)

    def test_large_values(self):
        self.assertEqual(perimeter(1e6, 1e6), 4e7)

    def test_small_values(self):
        self.assertEqual(perimeter(0.001, 0.001), 0.004)

    def test_float_values(self):
        self.assertAlmostEqual(perimeter(3.14, 2.71), 12.89)
