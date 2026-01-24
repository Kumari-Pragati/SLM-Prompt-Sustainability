import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(rombus_perimeter(3), 12)

    def test_zero(self):
        self.assertEqual(rombus_perimeter(0), 0)

    def test_negative_integer(self):
        self.assertEqual(rombus_perimeter(-1), 4)

    def test_float(self):
        self.assertAlmostEqual(rombus_perimeter(2.5), 16)

    def test_non_integer(self):
        self.assertRaises(TypeError, rombus_perimeter, 'string')
