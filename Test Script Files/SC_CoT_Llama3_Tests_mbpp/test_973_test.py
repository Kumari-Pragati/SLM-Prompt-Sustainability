import unittest
from mbpp_973_code import left_rotate

class TestLeftRotate(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(left_rotate("hello", 2), "llohe")

    def test_edge_case_start(self):
        self.assertEqual(left_rotate("hello", 5), "olleh")

    def test_edge_case_end(self):
        self.assertEqual(left_rotate("hello", 1), "hello")

    def test_edge_case_zero(self):
        self.assertEqual(left_rotate("hello", 0), "hello")

    def test_edge_case_long_string(self):
        self.assertEqual(left_rotate("hello world", 10), "worldhello")

    def test_edge_case_long_string_end(self):
        self.assertEqual(left_rotate("hello world", 12), "worldhello")

    def test_edge_case_long_string_zero(self):
        self.assertEqual(left_rotate("hello world", 0), "hello world")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            left_rotate(123, 2)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            left_rotate("hello", 7)
