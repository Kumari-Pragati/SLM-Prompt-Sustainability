import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):

    def test_positive_integer_arguments(self):
        """Test positive integer arguments"""
        self.assertEqual(ap_sum(1, 5, 1), 15)
        self.assertEqual(ap_sum(2, 3, 1), 10)
        self.assertEqual(ap_sum(3, 10, 2), 165)

    def test_zero_arguments(self):
        """Test zero arguments"""
        self.assertEqual(ap_sum(0, 0, 0), 0)

    def test_negative_integer_arguments(self):
        """Test negative integer arguments"""
        self.assertEqual(ap_sum(-1, 5, -1), -15)
        self.assertEqual(ap_sum(-2, -3, -1), -10)
        self.assertEqual(ap_sum(-3, 10, -2), -165)

    def test_non_integer_arguments(self):
        """Test non-integer arguments"""
        with self.assertRaises(TypeError):
            ap_sum(1.0, 5, 1)
        with self.assertRaises(TypeError):
            ap_sum(1, 5.0, 1)
        with self.assertRaises(TypeError):
            ap_sum(1, 5, 'd')

    def test_negative_n_arguments(self):
        """Test negative n argument"""
        with self.assertRaises(ValueError):
            ap_sum(1, -1, 1)

    def test_zero_d_arguments(self):
        """Test zero d argument"""
        with self.assertRaises(ValueError):
            ap_sum(1, 5, 0)
