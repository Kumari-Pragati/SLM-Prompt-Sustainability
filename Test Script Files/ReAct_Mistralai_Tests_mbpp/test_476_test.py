import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(big_sum([]), None)

    def test_single_element(self):
        """Test with a single element list"""
        for num in range(100):
            self.assertEqual(big_sum([num]), num)

    def test_positive_numbers(self):
        """Test with a list of positive numbers"""
        for num1 in range(100):
            for num2 in range(num1, 200):
                self.assertEqual(big_sum([num1, num2]), max([num1, num2]) + min([num1, num2]))

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        for num1 in range(-100, 0):
            for num2 in range(num1, -200, -1):
                self.assertEqual(big_sum([num1, num2]), max([num1, num2]) + min([num1, num2]))

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative numbers"""
        for num1 in range(-100, 100):
            for num2 in range(-100, 100):
                if num1 > num2:
                    self.assertEqual(big_sum([num1, num2]), max([num1, num2]) + min([num1, num2]))
                else:
                    self.assertEqual(big_sum([num1, num2]), max([num2, num1]) + min([num2, num1]))

    def test_min_max_same(self):
        """Test when min and max are the same"""
        for num in range(100):
            self.assertEqual(big_sum([num, num]), 2 * num)

    def test_min_max_zero(self):
        """Test when min and max are zero"""
        self.assertEqual(big_sum([0, 0]), 0)
