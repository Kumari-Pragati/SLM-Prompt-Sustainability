import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_zero_area(self):
        self.assertEqual(rectangle_area(0, 10), 0)
        self.assertEqual(rectangle_area(5, 0), 0)

    def test_negative_values(self):
        self.assertEqual(rectangle_area(-5, 10), -50)
        self.assertEqual(rectangle_area(5, -10), -50)

    def test_negative_and_zero_values(self):
        self.assertEqual(rectangle_area(-5, 0), 0)
        self.assertEqual(rectangle_area(0, -10), 0)

    def test_non_integer_values(self):
        self.assertEqual(rectangle_area(5.5, 10.5), 57.5)
        self.assertEqual(rectangle_area(5, 10.5), 52.5)
        self.assertEqual(rectangle_area(5.5, 10), 55)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rectangle_area("5", 10)
        with self.assertRaises(TypeError):
            rectangle_area(5, "10")
        with self.assertRaises(TypeError):
            rectangle_area("5", "10")
