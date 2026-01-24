import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(area_trapezium(3, 4, 5), 15.0)
        self.assertEqual(area_trapezium(6, 2, 1), 6.0)
        self.assertEqual(area_trapezium(1, 1, 1), 0.5)

    def test_zero_values(self):
        self.assertAlmostEqual(area_trapezium(0, 4, 5), 0.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(3, 0, 5), 0.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(3, 4, 0), 0.0, delta=0.01)

    def test_negative_values(self):
        self.assertAlmostEqual(area_trapezium(-3, 4, 5), 15.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(3, -4, 5), 15.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(3, 4, -5), 7.5, delta=0.01)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, area_trapezium, "base1", 4, 5)
        self.assertRaises(TypeError, area_trapezium, 3, "base2", 5)
        self.assertRaises(TypeError, area_trapezium, 3, 4, "height")
        self.assertRaises(TypeError, area_trapezium, -3, 4, -5)
        self.assertRaises(ValueError, area_trapezium, 0, 0, 0)
