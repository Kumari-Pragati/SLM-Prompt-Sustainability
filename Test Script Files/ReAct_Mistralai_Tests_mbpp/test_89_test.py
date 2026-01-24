import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_positive_integer(self):
        """Test closest_num with positive integer"""
        self.assertEqual(closest_num(5), 4)

    def test_zero(self):
        """Test closest_num with zero"""
        self.assertEqual(closest_num(0), -1)

    def test_negative_integer(self):
        """Test closest_num with negative integer"""
        self.assertEqual(closest_num(-5), -6)

    def test_large_positive_integer(self):
        """Test closest_num with large positive integer"""
        self.assertEqual(closest_num(1000), 999)

    def test_large_negative_integer(self):
        """Test closest_num with large negative integer"""
        self.assertEqual(closest_num(-1000), -1001)
