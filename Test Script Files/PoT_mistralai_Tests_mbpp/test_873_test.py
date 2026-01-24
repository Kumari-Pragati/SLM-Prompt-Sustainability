import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_base_case(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_typical_cases(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_edge_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)
        self.assertEqual(fibonacci(40), 102729370)
        self.assertEqual(fibonacci(50), 354224848179261915075)
