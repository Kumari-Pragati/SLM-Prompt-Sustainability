import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(15, 20), 300)

    def test_negative_numbers(self):
        self.assertEqual(rectangle_area(-5, -10), 50)
        self.assertEqual(rectangle_area(-15, -20), 300)

    def test_zero(self):
        self.assertEqual(rectangle_area(0, 10), 0)
        self.assertEqual(rectangle_area(15, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_non_integer_values(self):
        self.assertEqual(rectangle_area(2.5, 3.5), 8.75)
        self.assertEqual(rectangle_area(5, 4), 20)

    def test_string_values(self):
        with self.assertRaises(TypeError):
            rectangle_area("5", 10)
        with self.assertRaises(TypeError):
            rectangle_area(5, "10")
        with self.assertRaises(TypeError):
            rectangle_area("5", "10")
