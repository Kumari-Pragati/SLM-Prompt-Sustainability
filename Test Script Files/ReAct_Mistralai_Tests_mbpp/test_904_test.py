import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):

    def test_even_num_positive(self):
        """Test that even numbers return True"""
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(10))
        self.assertTrue(even_num(100))

    def test_even_num_zero(self):
        """Test that zero returns True"""
        self.assertTrue(even_num(0))

    def test_odd_num_negative(self):
        """Test that odd numbers return False"""
        self.assertFalse(even_num(1))
        self.assertFalse(even_num(3))
        self.assertFalse(even_num(5))

    def test_negative_numbers(self):
        """Test that negative numbers behave the same as positive numbers"""
        self.assertTrue(even_num(-2))
        self.assertTrue(even_num(-10))
        self.assertFalse(even_num(-1))

    def test_edge_cases(self):
        """Test edge cases: minimum and maximum integers"""
        self.assertTrue(even_num(-2147483648))
        self.assertTrue(even_num(2147483647))
