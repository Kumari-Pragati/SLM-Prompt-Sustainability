import unittest
from mbpp_84_code import sequence

class TestSequence(unittest.TestCase):

    def test_base_case_1(self):
        """Test base case 1: n = 1"""
        self.assertEqual(sequence(1), 1)

    def test_base_case_2(self):
        """Test base case 2: n = 2"""
        self.assertEqual(sequence(2), 1)

    def test_positive_integer(self):
        """Test positive integers greater than 2"""
        for n in range(3, 10):
            self.assertEqual(sequence(n), sequence(sequence(n-1)) + sequence(n-sequence(n-1)))

    def test_negative_integer(self):
        """Test negative integers"""
        for n in [-1, -2]:
            with self.assertRaises(ValueError):
                sequence(n)

    def test_zero(self):
        """Test zero"""
        with self.assertRaises(ValueError):
            sequence(0)

    def test_float(self):
        """Test float"""
        with self.assertRaises(TypeError):
            sequence(3.14)

    def test_string(self):
        """Test string"""
        with self.assertRaises(TypeError):
            sequence('abc')
