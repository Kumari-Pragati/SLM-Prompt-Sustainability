import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_positive_numbers(self):
        """Test find_star_num with positive numbers"""
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 7)
        self.assertEqual(find_star_num(10), 301)

    def test_zero(self):
        """Test find_star_num with zero"""
        self.assertEqual(find_star_num(0), 1)

    def test_negative_numbers(self):
        """Test find_star_num with negative numbers"""
        self.assertEqual(find_star_num(-1), -3)
        self.assertEqual(find_star_num(-2), -13)
        self.assertEqual(find_star_num(-10), 1301)

    def test_large_numbers(self):
        """Test find_star_num with large numbers"""
        self.assertEqual(find_star_num(100), 6000000001)
        self.assertEqual(find_star_num(1000), 6000000000001)
