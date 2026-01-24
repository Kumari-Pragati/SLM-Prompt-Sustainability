import unittest
from mbpp_112_code import skip
from math import sqrt

class TestPerimeter(unittest.TestCase):

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(10, 5), 30)
        self.assertEqual(perimeter(2, 1), 6)
        self.assertEqual(perimeter(sqrt(8), sqrt(2)), 10)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-10, 5), 20)
        self.assertEqual(perimeter(10, -5), 20)
        self.assertRaises(ValueError, lambda: perimeter(-10, -5))

    @skip("Not handling the case where the diameter is less than the height")
    def test_perimeter_invalid_diameter_less_than_height(self):
        pass
