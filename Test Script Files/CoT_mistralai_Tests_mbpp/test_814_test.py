import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rombus_area(3, 4), 6.0)
        self.assertEqual(rombus_area(5, 10), 25.0)

    def test_zero(self):
        self.assertEqual(rombus_area(0, 5), 0.0)
        self.assertEqual(rombus_area(5, 0), 0.0)

    def test_negative_numbers(self):
        self.assertEqual(rombus_area(-3, 4), 6.0)
        self.assertEqual(rombus_area(3, -4), 6.0)

    def test_one_zero(self):
        self.assertEqual(rombus_area(0, 5), 0.0)
        self.assertEqual(rombus_area(5, 0), 0.0)
        self.assertEqual(rombus_area(3, 0), 0.0)
        self.assertEqual(rombus_area(0, 3), 0.0)
