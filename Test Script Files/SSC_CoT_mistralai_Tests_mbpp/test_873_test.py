import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_small_positive(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)

    def test_fibonacci_large_positive(self):
        self.assertEqual(fibonacci(45), 75708813)
        self.assertEqual(fibonacci(50), 12586269025)

    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), None)

    def test_fibonacci_negative(self):
        self.assertEqual(fibonacci(-1), None)
        self.assertEqual(fibonacci(-2), None)
        self.assertEqual(fibonacci(-3), None)
