import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_trapezium(5, 10, 7), 47.5)

    def test_zero_height(self):
        self.assertEqual(area_trapezium(5, 10, 0), 0)

    def test_negative_heights(self):
        self.assertEqual(area_trapezium(5, 10, -7), 0)

    def test_negative_bases(self):
        self.assertAlmostEqual(area_trapezium(-5, -10, 7), 47.5)

    def test_zero_bases(self):
        self.assertEqual(area_trapezium(0, 0, 7), 0)

    def test_negative_and_zero_bases(self):
        self.assertAlmostEqual(area_trapezium(-5, 0, 7), 17.5)

    def test_equal_bases(self):
        self.assertAlmostEqual(area_trapezium(5, 5, 7), 35)

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            area_trapezium("5", 10, 7)
        with self.assertRaises(TypeError):
            area_trapezium(5, "10", 7)
        with self.assertRaises(TypeError):
            area_trapezium(5, 10, "7")

    def test_invalid_input_values(self):
        with self.assertRaises(ValueError):
            area_trapezium(-5, 10, 7)
        with self.assertRaises(ValueError):
            area_trapezium(5, -10, 7)
        with self.assertRaises(ValueError):
            area_trapezium(5, 10, -7)
