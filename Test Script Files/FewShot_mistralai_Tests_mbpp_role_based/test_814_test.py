import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rombus_area(3, 4), 6.0)
        self.assertEqual(rombus_area(5, 5), 12.5)

    def test_zero(self):
        self.assertEqual(rombus_area(0, 0), 0.0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, rombus_area, -1, 2)
        self.assertRaises(ValueError, rombus_area, 1, -2)
