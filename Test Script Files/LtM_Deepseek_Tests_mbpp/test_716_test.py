import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(rombus_perimeter(5), 20)

    def test_zero(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_negative_integer(self):
        self.assertEqual(rombus_perimeter(-3), -12)

    def test_large_number(self):
        self.assertEqual(rombus_perimeter(10000), 40000)

    def test_decimal(self):
        self.assertAlmostEqual(rombus_perimeter(2.5), 10.0)

    def test_negative_decimal(self):
        self.assertAlmostEqual(rombus_perimeter(-2.5), -10.0)

    def test_large_decimal(self):
        self.assertAlmostEqual(rombus_perimeter(1234.56), 4938.24)
