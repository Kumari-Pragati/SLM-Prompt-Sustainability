import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(left_rotate("hello", 2), "llohe")

    def test_edge_case_d_zero(self):
        self.assertEqual(left_rotate("hello", 0), "hello")

    def test_edge_case_d_equal_to_length(self):
        self.assertEqual(left_rotate("hello", 5), "hello")

    def test_edge_case_d_greater_than_length(self):
        self.assertEqual(left_rotate("hello", 6), "hello")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            left_rotate("hello", "a")

    def test_invalid_input_negative_integer(self):
        with self.assertRaises(TypeError):
            left_rotate("hello", -1)
