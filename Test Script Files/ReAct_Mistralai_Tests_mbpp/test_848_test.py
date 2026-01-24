import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(area_trapezium(3, 4, 5), 15.0)
        self.assertEqual(area_trapezium(1, 1, 1), 0.5)
        self.assertEqual(area_trapezium(10, 20, 5), 100.0)

    def test_zero_values(self):
        self.assertAlmostEqual(area_trapezium(0, 4, 5), 0.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(4, 0, 5), 0.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(0, 0, 5), 0.0, delta=0.01)

    def test_negative_values(self):
        self.assertAlmostEqual(area_trapezium(-3, 4, 5), 15.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(3, -4, 5), 15.0, delta=0.01)
        self.assertAlmostEqual(area_trapezium(-3, -4, 5), 15.0, delta=0.01)

    def test_non_numeric_values(self):
        self.assertRaises(TypeError, area_trapezium, 'a', 'b', 5)
        self.assertRaises(TypeError, area_trapezium, 3, 'b', 5)
        self.assertRaises(TypeError, area_trapezium, 3, 4, 'a')
