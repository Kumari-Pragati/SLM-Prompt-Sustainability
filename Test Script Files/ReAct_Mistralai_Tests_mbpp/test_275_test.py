import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_positive_numbers(self):
        """Test get_Position with positive numbers"""
        data = [(range(1, 6), 3, 2, 2),
                ([1, 2, 3, 4, 5], 3, 2, 4),
                ([10, 20, 30, 40, 50], 5, 10, 5)]
        for test_data in data:
            with self.subTest(test_data=test_data):
                result = get_Position(*test_data)
                self.assertEqual(result, test_data[3] + 1)

    def test_zero_or_negative_numbers(self):
        """Test get_Position with zero or negative numbers"""
        data = [([0, -1, 2], 3, 2, -1),
                ([-1, 0, 1], 3, 2, -1),
                ([0, 0, 0], 3, 2, -1)]
        for test_data in data:
            with self.subTest(test_data=test_data):
                result = get_Position(*test_data)
                self.assertEqual(result, -1)

    def test_empty_list(self):
        """Test get_Position with an empty list"""
        data = ([], 3, 2)
        with self.subTest(test_data=data):
            result = get_Position(*data)
            self.assertEqual(result, -1)

    def test_single_element_list(self):
        """Test get_Position with a single-element list"""
        data = ([1], 3, 2)
        with self.subTest(test_data=data):
            result = get_Position(*data)
            self.assertEqual(result, 1)

    def test_single_digit_numbers(self):
        """Test get_Position with single-digit numbers"""
        data = ([1, 2, 3, 4, 5], 1, 10)
        with self.subTest(test_data=data):
            result = get_Position(*data)
            self.assertEqual(result, -1)

    def test_large_numbers(self):
        """Test get_Position with large numbers"""
        data = ([1000000001, 2000000002, 3000000003, 4000000004, 5000000005], 5, 1000000007)
        with self.subTest(test_data=data):
            result = get_Position(*data)
            self.assertEqual(result, 5)
