import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    def test_perimeter_positive_numbers(self):
        self.assertEqual(perimeter(10, 5), 30)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_negative_numbers(self):
        self.assertEqual(perimeter(-10, -5), 20)

    def test_perimeter_mixed_numbers(self):
        self.assertEqual(perimeter(5, -3), 16)
