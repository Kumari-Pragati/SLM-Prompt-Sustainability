import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_rombus_perimeter_positive(self):
        self.assertEqual(rombus_perimeter(1), 4)
        self.assertEqual(rombus_perimeter(2), 8)
        self.assertEqual(rombus_perimeter(3), 12)
        self.assertEqual(rombus_perimeter(4), 16)
        self.assertEqual(rombus_perimeter(5), 20)

    def test_rombus_perimeter_zero(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_rombus_perimeter_negative(self):
        self.assertEqual(rombus_perimeter(-1), -4)
        self.assertEqual(rombus_perimeter(-2), -8)
        self.assertEqual(rombus_perimeter(-3), -12)
        self.assertEqual(rombus_perimeter(-4), -16)
        self.assertEqual(rombus_perimeter(-5), -20)
