import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_empty_dict(self):
        """Test if function returns 0 for an empty dictionary"""
        self.assertEqual(return_sum({}), 0)

    def test_single_value_dict(self):
        """Test if function correctly returns a single value from a dictionary"""
        self.assertEqual(return_sum({'a': 1}), 1)

    def test_multiple_values_dict(self):
        """Test if function correctly returns the sum of multiple values from a dictionary"""
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_negative_values(self):
        """Test if function correctly handles negative values"""
        self.assertEqual(return_sum({'a': -1, 'b': 2}), 1)

    def test_mixed_values(self):
        """Test if function correctly handles a mix of positive and negative values"""
        self.assertEqual(return_sum({'a': 1, 'b': -2, 'c': 3}), 2)

    def test_key_error(self):
        """Test if function correctly handles a key error"""
        with self.assertRaises(KeyError):
            return_sum({'a': 1, 'b': 2, 'c': 3, 'non_existent_key': 4})
