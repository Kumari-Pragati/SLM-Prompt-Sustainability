import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_perimeter_with_positive_numbers(self):
        self.assertEqual(perimeter(4, 5), 18)
        self.assertEqual(perimeter(10, 20), 60)
        self.assertEqual(perimeter(5.5, 3.3), 13.6)

    def test_perimeter_with_zero(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(4, 0), 8)

    def test_perimeter_with_negative_numbers(self):
        self.assertEqual(perimeter(-4, 5), 6)
        self.assertEqual(perimeter(10, -20), 0)

    def test_perimeter_with_non_numbers(self):
        with self.assertRaises(TypeError):
            perimeter("4", 5)
        with self.assertRaises(TypeError):
            perimeter(4, "5")
        with self.assertRaises(TypeError):
            perimeter("4", "5")
