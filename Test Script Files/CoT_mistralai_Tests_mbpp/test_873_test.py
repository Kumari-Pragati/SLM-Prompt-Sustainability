import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_positive_numbers(self):
        for n in range(3, 11):
            self.assertEqual(fibonacci(n), fibonacci_iterative(n))

    def test_large_number(self):
        self.assertEqual(fibonacci(45), 1134903170)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            fibonacci(0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            fibonacci(3.14)

def fibonacci_iterative(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[-1]
