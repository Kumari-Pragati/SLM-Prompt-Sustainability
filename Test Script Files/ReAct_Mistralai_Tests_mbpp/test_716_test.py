import unittest
from mbpp_716_code import rombus_perimeter

class TestRombusPerimeter(unittest.TestCase):

    def test_rombus_perimeter_positive(self):
        """Test rombus_perimeter with positive integer"""
        self.assertEqual(rombus_perimeter(3), 12)

    def test_rombus_perimeter_zero(self):
        """Test rombus_perimeter with zero"""
        self.assertEqual(rombus_perimeter(0), 0)

    def test_rombus_perimeter_negative(self):
        """Test rombus_perimeter with negative integer"""
        self.assertRaises(ValueError, rombus_perimeter, -5)

    def test_rombus_perimeter_float(self):
        """Test rombus_perimeter with float"""
        self.assertAlmostEqual(rombus_perimeter(2.5), 16, delta=0.01)

    def test_rombus_perimeter_non_number(self):
        """Test rombus_perimeter with non-number"""
        self.assertRaises(TypeError, rombus_perimeter, "string")
