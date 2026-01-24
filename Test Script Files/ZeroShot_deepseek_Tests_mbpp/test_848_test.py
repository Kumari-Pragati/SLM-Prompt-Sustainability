import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(area_trapezium(5, 10, 7), 47.5)

    def test_negative_numbers(self):
        self.assertAlmostEqual(area_trapezium(-5, -10, 7), -47.5)

    def test_zero_height(self):
        self.assertEqual(area_trapezium(5, 10, 0), 0)

    def test_zero_bases(self):
        self.assertEqual(area_trapezium(0, 0, 7), 0)

    def test_equal_bases(self):
        self.assertEqual(area_trapezium(5, 5, 7), 35)

    def test_zero_bases_and_height(self):
        self.assertEqual(area_trapezium(0, 0, 0), 0)
