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
        self.assertRaises(Exception, area_trapezium, -5, -10, 7)

    def test_negative_height(self):
        self.assertRaises(Exception, area_trapezium, 5, 10, -7)

    def test_equal_bases(self):
        self.assertAlmostEqual(area_trapezium(5, 5, 7), 35)

    def test_large_numbers(self):
        self.assertAlmostEqual(area_trapezium(10000, 20000, 3000), 230000000.0)
