import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_typical(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_edge(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_negative(self):
        with self.assertRaises(TypeError):
            fibonacci(-1)

    def test_fibonacci_non_integer(self):
        with self.assertRaises(TypeError):
            fibonacci('a')
