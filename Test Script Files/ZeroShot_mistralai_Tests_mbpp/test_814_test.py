import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_rombus_area_with_positive_numbers(self):
        self.assertEqual(rombus_area(3, 4), 6.0)
        self.assertEqual(rombus_area(5, 12), 30.0)
        self.assertEqual(rombus_area(10, 20), 100.0)

    def test_rombus_area_with_zero(self):
        self.assertEqual(rombus_area(0, 4), 0.0)
        self.assertEqual(rombus_area(3, 0), 0.0)

    def test_rombus_area_with_negative_numbers(self):
        self.assertEqual(rombus_area(-3, 4), 0.0)
        self.assertEqual(rombus_area(3, -4), 0.0)
