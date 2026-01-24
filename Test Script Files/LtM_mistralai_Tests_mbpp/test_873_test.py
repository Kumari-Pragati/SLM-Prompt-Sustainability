import unittest
from mbpp_873_code import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_simple_input_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_simple_input_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_simple_input_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_edge_input_1(self):
        self.assertEqual(fibonacci(4), 3)

    def test_edge_input_2(self):
        self.assertEqual(fibonacci(5), 5)

    def test_edge_input_3(self):
        self.assertEqual(fibonacci(6), 8)

    def test_edge_input_4(self):
        self.assertEqual(fibonacci(7), 13)

    def test_edge_input_5(self):
        self.assertEqual(fibonacci(8), 21)

    def test_edge_input_6(self):
        self.assertEqual(fibonacci(9), 34)

    def test_edge_input_7(self):
        self.assertEqual(fibonacci(10), 55)

    def test_negative_input(self):
        self.assertRaises(ValueError, fibonacci, -1)

    def test_zero_input(self):
        self.assertRaises(ValueError, fibonacci, 0)
