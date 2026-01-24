import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_edge_conditions(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(-1), 1)

    def test_complex_cases(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
