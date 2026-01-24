import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_positive_values(self):
        """Test finding volume with positive values"""
        self.assertEqual(find_Volume(3, 4, 5), 60.0)
        self.assertEqual(find_Volume(2, 2, 2), 8.0)
        self.assertEqual(find_Volume(1, 1, 1), 1.0)

    def test_zero_values(self):
        """Test finding volume with zero values"""
        self.assertEqual(find_Volume(0, 0, 0), 0.0)
        self.assertRaises(ValueError, find_Volume, 0, 0, -1)

    def test_negative_values(self):
        """Test finding volume with negative values"""
        self.assertRaises(ValueError, find_Volume, -1, 2, 3)
        self.assertRaises(ValueError, find_Volume, 2, -1, 3)
        self.assertRaises(ValueError, find_Volume, 2, 3, -1)
