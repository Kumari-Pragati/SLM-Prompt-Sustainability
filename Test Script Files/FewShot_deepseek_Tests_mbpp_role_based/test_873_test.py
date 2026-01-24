import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(fibonacci(5), 5)

    def test_boundary_condition(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)

    def test_edge_condition(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fibonacci('a')
        with self.assertRaises(ValueError):
            fibonacci(-1)
