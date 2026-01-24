import unittest
from mbpp_814_code import rombus_area

class TestRombusArea(unittest.TestCase):

    def test_positive_numbers(self):
        """Test rombus_area with positive numbers"""
        self.assertEqual(rombus_area(3, 4), 6.0)
        self.assertEqual(rombus_area(5, 5), 12.5)

    def test_zero(self):
        """Test rombus_area with zero as one of the inputs"""
        self.assertEqual(rombus_area(0, 4), 0.0)
        self.assertEqual(rombus_area(4, 0), 0.0)

    def test_negative_numbers(self):
        """Test rombus_area with negative numbers"""
        self.assertEqual(rombus_area(-3, 4), 6.0)
        self.assertRaises(ValueError, lambda: rombus_area(-3, -4))

    def test_edge_case_one_zero(self):
        """Test rombus_area with one zero"""
        self.assertEqual(rombus_area(0, 5), 0.0)
        self.assertEqual(rombus_area(5, 0), 0.0)
