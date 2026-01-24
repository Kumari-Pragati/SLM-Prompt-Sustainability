import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)

    def test_edge_cases(self):
        self.assertEqual(fibonacci(0), 1)  # Edge case: Fibonacci of 0
        self.assertEqual(fibonacci(-1), 1)  # Edge case: Negative input

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            fibonacci('a')  # Error case: Non-integer input
        with self.assertRaises(TypeError):
            fibonacci(None)  # Error case: None input
