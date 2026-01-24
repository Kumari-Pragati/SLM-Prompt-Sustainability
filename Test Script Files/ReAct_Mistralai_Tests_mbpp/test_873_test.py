import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_base_case_1(self):
        """Test fibonacci function with input 1"""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_base_case_2(self):
        """Test fibonacci function with input 2"""
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_small_input(self):
        """Test fibonacci function with small inputs"""
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_large_input(self):
        """Test fibonacci function with large inputs"""
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_fibonacci_negative_input(self):
        """Test fibonacci function with negative inputs"""
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_zero_input(self):
        """Test fibonacci function with zero input"""
        with self.assertRaises(ValueError):
            fibonacci(0)
