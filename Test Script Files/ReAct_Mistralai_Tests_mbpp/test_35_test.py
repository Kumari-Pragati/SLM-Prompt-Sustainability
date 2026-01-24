import unittest
from mbpp_35_code import find_rect_num

class TestFindRectNum(unittest.TestCase):

    def test_positive_integer(self):
        """Test find_rect_num with a positive integer"""
        self.assertEqual(find_rect_num(3), 12)

    def test_zero(self):
        """Test find_rect_num with zero"""
        self.assertEqual(find_rect_num(0), 0)

    def test_negative_integer(self):
        """Test find_rect_num with a negative integer"""
        self.assertEqual(find_rect_num(-3), 0)

    def test_large_integer(self):
        """Test find_rect_num with a large integer"""
        self.assertEqual(find_rect_num(100), 10001)

    def test_float(self):
        """Test find_rect_num with a float"""
        with self.assertRaises(TypeError):
            find_rect_num(3.14)
