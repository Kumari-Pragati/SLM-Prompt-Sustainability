import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_simple_multiplication(self):
        self.assertEqual(multiply_int(2, 3), 6)
        self.assertEqual(multiply_int(-2, 3), -6)
        self.assertEqual(multiply_int(2, -3), -6)
        self.assertEqual(multiply_int(-2, -3), 6)

    def test_edge_cases(self):
        self.assertEqual(multiply_int(0, 0), 0)
        self.assertEqual(multiply_int(1, 0), 0)
        self.assertEqual(multiply_int(0, 1), 0)
        self.assertEqual(multiply_int(1, 1), 1)

    def test_recursion_limit(self):
        self.assertRaises(RecursionError, lambda: multiply_int(10, 100000))
