import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_first_two_numbers(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_typical_cases(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_large_numbers(self):
        self.assertEqual(fibonacci(20), 6765)

    def test_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            fibonacci(1000)
