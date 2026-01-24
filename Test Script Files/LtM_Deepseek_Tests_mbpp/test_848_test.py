import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_trapezium(5, 10, 7), 47.5)

    def test_zero_height(self):
        self.assertEqual(area_trapezium(5, 10, 0), 0)

    def test_zero_bases(self):
        self.assertEqual(area_trapezium(0, 0, 10), 0)

    def test_negative_bases(self):
        self.assertEqual(area_trapezium(-5, -10, 7), -47.5)

    def test_negative_height(self):
        self.assertEqual(area_trapezium(5, 10, -7), 0)

    def test_equal_bases(self):
        self.assertEqual(area_trapezium(5, 5, 7), 25)

    def test_large_numbers(self):
        self.assertAlmostEqual(area_trapezium(1000000, 2000000, 30000), 23050000000.0)
