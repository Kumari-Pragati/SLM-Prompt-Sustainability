import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_positive_diameter_and_height(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_zero_diameter_and_height(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_negative_diameter_and_height(self):
        self.assertEqual(perimeter(-3, -4), 14)

    def test_negative_diameter_and_positive_height(self):
        self.assertEqual(perimeter(-3, 4), 14)

    def test_positive_diameter_and_negative_height(self):
        self.assertEqual(perimeter(3, -4), 14)
