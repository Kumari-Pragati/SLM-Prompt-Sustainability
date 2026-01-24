import unittest
from mbpp_458_code import rectangle_area

class TestRectangleArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_zero_area(self):
        self.assertEqual(rectangle_area(0, 10), 0)
        self.assertEqual(rectangle_area(5, 0), 0)

    def test_negative_area(self):
        self.assertEqual(rectangle_area(-5, 10), -50)
        self.assertEqual(rectangle_area(5, -10), -50)

    def test_large_numbers(self):
        self.assertEqual(rectangle_area(1000000000, 1000000000), 1000000000000000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rectangle_area("5", 10)
        with self.assertRaises(TypeError):
            rectangle_area(5, "10")
        with self.assertRaises(TypeError):
            rectangle_area("5", "10")
