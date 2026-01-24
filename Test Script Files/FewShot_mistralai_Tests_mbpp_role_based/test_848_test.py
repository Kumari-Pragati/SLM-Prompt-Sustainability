import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):
    def test_positive_base_and_height(self):
        self.assertEqual(area_trapezium(2, 4, 3), 12.0)

    def test_zero_base_and_height(self):
        self.assertEqual(area_trapezium(0, 0, 0), 0.0)

    def test_negative_base_and_height(self):
        self.assertEqual(area_trapezium(-2, -4, -3), 6.0)

    def test_zero_and_positive_height(self):
        self.assertEqual(area_trapezium(0, 4, 3), 6.0)

    def test_positive_and_zero_height(self):
        self.assertEqual(area_trapezium(2, 4, 0), 8.0)

    def test_negative_base_and_positive_height(self):
        self.assertEqual(area_trapezium(-2, 4, 3), 12.0)

    def test_invalid_base1(self):
        with self.assertRaises(ValueError):
            area_trapezium(-1, 4, 3)

    def test_invalid_base2(self):
        with self.assertRaises(ValueError):
            area_trapezium(2, -1, 3)
