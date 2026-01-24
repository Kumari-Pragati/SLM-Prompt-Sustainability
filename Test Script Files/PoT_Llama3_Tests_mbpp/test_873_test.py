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
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(fibonacci(0), None)
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

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            fibonacci('a')
        with self.assertRaises(TypeError):
            fibonacci(None)
        with self.assertRaises(TypeError):
            fibonacci(0.5)
