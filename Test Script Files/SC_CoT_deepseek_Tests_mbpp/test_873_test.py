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

    def test_boundary_conditions(self):
        self.assertEqual(fibonacci(0), 1)  # 0 is a valid input, but it's not in the fibonacci sequence

    def test_edge_cases(self):
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)

    def test_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            fibonacci(873_code.MAX_FIBONACCI_INDEX + 1)
