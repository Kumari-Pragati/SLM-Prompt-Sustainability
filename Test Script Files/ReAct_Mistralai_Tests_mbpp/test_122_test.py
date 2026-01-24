import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):

    def test_empty_list(self):
        """Test when n is 0"""
        self.assertEqual(smartNumber(0), [])

    def test_single_element(self):
        """Test when n is 1"""
        self.assertEqual(smartNumber(1), [2])

    def test_multiple_elements(self):
        """Test when n is less than the number of primes"""
        self.assertEqual(smartNumber(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_last_element(self):
        """Test when n is equal to the number of primes"""
        self.assertEqual(smartNumber(len(smartNumber(10))), 313)

    def test_out_of_range(self):
        """Test when n is greater than the number of primes"""
        with self.assertRaises(IndexError):
            smartNumber(len(smartNumber(10)) + 1)
