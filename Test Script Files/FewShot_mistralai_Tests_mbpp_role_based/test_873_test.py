import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_first_two_numbers(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_small_positive_numbers(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)

    def test_large_positive_numbers(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, fibonacci, -1)
        self.assertRaises(ValueError, fibonacci, -2)
