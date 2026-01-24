import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(rombus_area(5, 10), 25.0)
        self.assertAlmostEqual(rombus_area(15, 20), 150.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(rombus_area(-5, 10), -25.0)
        self.assertAlmostEqual(rombus_area(-15, 20), -150.0)

    def test_zero(self):
        self.assertEqual(rombus_area(0, 10), 0)
        self.assertEqual(rombus_area(15, 0), 0)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(rombus_area(2.5, 3.5), 4.375)
        self.assertAlmostEqual(rombus_area(7.5, 12.5), 46.875)
