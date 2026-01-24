import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_positive_multiply(self):
        self.assertEqual(multiply_int(2, 3), 6)

    def test_negative_multiply(self):
        self.assertEqual(multiply_int(-2, 3), -6)

    def test_zero_multiply(self):
        self.assertEqual(multiply_int(2, 0), 0)

    def test_one_multiply(self):
        self.assertEqual(multiply_int(2, 1), 2)

    def test_large_multiply(self):
        self.assertEqual(multiply_int(100, 200), 20000)

    def test_negative_large_multiply(self):
        self.assertEqual(multiply_int(-100, 200), -20000)

    def test_edge_case_multiply(self):
        self.assertEqual(multiply_int(0, 0), 0)

    def test_invalid_input_multiply(self):
        with self.assertRaises(TypeError):
            multiply_int('a', 2)
