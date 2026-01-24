import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_typical(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_edge(self):
        self.assertEqual(fibonacci(0), 1)
        self.assertEqual(fibonacci(-1), None)
        self.assertEqual(fibonacci(-2), None)

    def test_fibonacci_invalid(self):
        with self.assertRaisesRecursionError:
            fibonacci(1000)
