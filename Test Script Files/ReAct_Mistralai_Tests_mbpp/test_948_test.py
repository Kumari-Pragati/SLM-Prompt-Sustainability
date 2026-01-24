import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):

    def test_get_item_positive_index(self):
        """Test getting item with valid positive index"""
        test_tuple = (1, 2, 3, 4, 5)
        expected_result = 3
        self.assertEqual(get_item(test_tuple, 2), expected_result)

    def test_get_item_zero_index(self):
        """Test getting item with zero index"""
        test_tuple = (1, 2, 3, 4, 5)
        expected_result = 1
        self.assertEqual(get_item(test_tuple, 0), expected_result)

    def test_get_item_negative_index(self):
        """Test getting item with negative index"""
        test_tuple = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(test_tuple, -1)

    def test_get_item_out_of_range_index(self):
        """Test getting item with index greater than tuple length"""
        test_tuple = (1, 2, 3, 4, 5)
        with self.assertRaises(IndexError):
            get_item(test_tuple, 6)

    def test_get_item_empty_tuple(self):
        """Test getting item from empty tuple"""
        test_tuple = ()
        with self.assertRaises(IndexError):
            get_item(test_tuple, 0)
