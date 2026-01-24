import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_small_numbers(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_larger_numbers(self):
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)

    def test_fibonacci_invalid_input(self):
        with self.assertRaisesRecursionLimitError:
            fibonacci(1000)
